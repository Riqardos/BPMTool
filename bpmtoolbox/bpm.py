import re
import sys, getopt


class BPMApp:
    """
    BPM tool
    Functions:
    - .get_all_snapshots()
    - .clean_snapshots() -> clean snapshots based on conditions
    """

    def __init__(self, acronym=None):
        self.acronym = acronym

    def get_all_snapshots(self):
        """Return list of objects"""
        output = self.get_all_snapshots_from_bpm()
        all_snapshots = self.parse_bpm_output(output)
        return all_snapshots

    def get_all_snapshots_formatted(self):
        """Print formatted info about snapshots"""
        all_snapshots = self.get_all_snapshots()
        print("All snapshots: \n")
        for snap in all_snapshots:
            print('AcronymId: ' + snap.acronym)
            print('State: ' + snap.state)
            print('Default: ' + snap.is_default)
            print('Number of instances: ' + snap.no_of_running_instances)
            print('\n')

        return all_snapshots

    def generate_stats(self, snapshots):
        stats = {}

        for snapshot in snapshots:
            try:
                state = snapshot.state
                state_acronyms = state + '_acronyms'
                acronym = snapshot.acronym
                no_instances = snapshot.no_of_running_instances

                if state in stats.keys():
                    stats[state] += 1
                    stats[state_acronyms] += [(acronym, no_instances)]
                else:
                    stats[state] = 1
                    stats[state_acronyms] = [(acronym, no_instances)]

            except Exception:
                print(str(Exception))


        return stats

    def get_snapshots_stat(self):
        """Return list of objects"""
        output = self.get_all_snapshots_from_bpm()
        all_snapshots = self.parse_bpm_output(output)
        stats = self.generate_stats(all_snapshots)
        print("Stats: " + self.acronym)
        print("Active: " + str(stats['State[Active]']) + "; " + str(stats['State[Active]_acronyms']))
        print("Nonactive: " + str(stats['State[Inactive]']) + "; " + str(stats['State[Inactive]_acronyms']))

        print("\nhelp: [(acronymId, NoRunningInstances)]")

    def clean_snapshots(self):
        all_snapshots = self.get_all_snapshots()
        filtered_snapshots = self.filter_snapshots(all_snapshots)

        all_snapshots = len(filtered_snapshots)
        deleted = 0
        counter = 1
        print("Deleting " + str(all_snapshots) + " instances...")
        print("#" * 30)
        for snapshot in filtered_snapshots:
            print("Processing " + "\t\t\t" + str(counter) + " / " + str(all_snapshots))
            try:
                AdminTask.BPMDeleteSnapshot(
                    '[-containerAcronym ' + self.acronym + ' -containerSnapshotAcronyms ' + snapshot.acronym + ' ]')
                deleted += 1
                print("Deleted: " + snapshot.acronym)
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print("Skipped:" + snapshot.acronym)
                print("Error: " + str(exc_obj))

            print('\n\n')
            counter += 1

        print("#" * 30)
        print("\n\nDeleted: " + str(deleted))
        print("Skipped: " + str(all_snapshots - deleted))

    def get_all_snapshots_from_bpm(self):
        return AdminTask.BPMShowProcessApplication('[-containerAcronym ' + self.acronym + ' ]')

    def filter_snapshots(cls, snapshots):
        """Filter snapshosts based on condition"""

        return list(filter(lambda s: (
                s.state == 'State[Inactive]' and
                s.no_of_running_instances == '0' and
                s.is_default == 'false'
        ), snapshots))

    def parse_bpm_output(cls, output):
        """Output parser"""

        # todo check what is returned if snapshot list is empty
        snapshots = output.replace('\t', '').split('List of Snapshots: \n')[1].split('\n\n')
        results = []
        if snapshots:

            for snapshot in snapshots:
                if snapshot != '':
                    dict_item = {}
                    for attribute in snapshot.split('\n'):
                        key, value = attribute.split(': ')
                        dict_item[key] = value

                    results.append(cls.SnapShot(**dict_item))

        return results

    class SnapShot:

        def __init__(self, **kwargs):
            """
            :param kwargs: dict
            {
              'Name': 'sn_for_Hursley',
              'Acronym': 'SFH',
              'Created On': '2014-05-12 14:05:08.563',
              'Created By': 'User.9',
              'Is Default': 'false',
              'State': 'State[Inactive]',
              'Capability': 'Capability[Standard]',
              'No of running instances': '0'
            }

            creates attributes by lowercasing key and removing spaces
            e.g.
                name: -> str
                acronym: -> str
                created_on: -> str
                created_by: -> str
                is_default: -> str
                state: -> str
                capability: -> str
                no_of_running_instances -> str

            """
            for key, value in kwargs.items():
                setattr(self, re.sub(r'[ ]', '_', key).lower(), value)

        def __str__(self):
            return str(vars(self))


if __name__ == '__main__':


    if len(sys.argv) != 3:
        print("Invalid number of arguments: two argument allowed: bpm.py <acronymId> [-hsld], see --help for more info")
        sys.exit(1)

    app_acronym = sys.argv[1]
    argv = sys.argv[2:]

    # validation
    valid_options = ['--help', '--stat', '--list', '--delete']
    valid_options_short = list(map(lambda x: x[1:3], valid_options))
    arg = argv[0]
    if len(arg) == 2:
        if arg not in valid_options_short:
            print("Invalid argument: " + arg + ", see --help")
            sys.exit(1)
    else:
        if arg not in valid_options:
            print("Invalid argument: " + arg + ", see --help")
            sys.exit(1)

    # functions switch
    try:
        bpm_tool = BPMApp(app_acronym)
        arg_trim = arg.replace('-', '')[0]
        if arg_trim == 'h':
            print("""
================================================================
HELP
================================================================
SYNOPSIS
bpm.py <acronymId> [-hsld]

OPTIONS
number of allowed arguments: 2

-h, --help      shows help
-l, --list      shows list of snapshots
-s, --stat      shows stats 
-d, --delete    will delete all snapshots, 
                based on condition(inactive, no_instancec=0, default=false )
            """)
        elif arg_trim == 's':
            bpm_tool.get_snapshots_stat()
        elif arg_trim == 'l':
            bpm_tool.get_all_snapshots_formatted()
        elif arg_trim == 'd':
            bpm_tool.clean_snapshots()

    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print("Error:\n" + str(exc_obj))