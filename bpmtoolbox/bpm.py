import re


class BPMTool:
    """
    BPM tool
    Functions:
    - .get_all_snapshots() -> get all snapshots
    - .clean_snapshots() -> no clean snapshots based on conditions
    """

    def __init__(self, acronym=None):
        self.acronym = acronym

    def get_all_snapshots(self):
        output = self.get_snapshots_from_bpm()
        all_snapshots = self.parse_output(output)
        return all_snapshots

    def clean_snapshots(self):
        all_snapshots = self.get_all_snapshots()
        filtered_snapshots = self.get_snapshots_to_clean(all_snapshots)

        for snapshot in filtered_snapshots:
            try:
                AdminTask.BPMSnapshotCleanup(
                    f'[-containerAcronym {self.acronym} -containerTrackAcronym {snapshot.acronym}]')
            except Exception as e:
                print(f"CLEANUP ERROR\nAcronym{snapshot}\nError:\n{str(e)}\n\n")

    def get_snapshots_from_bpm(self) -> str:
        return AdminTask.BPMShowProcessApplication(f'[-containerAcronym {self.acronym}]')

    @classmethod
    def get_snapshots_to_clean(cls, snapshots: list) -> list:
        """Filter snapshosts based on condition"""

        return list(filter(lambda s: (
                s.state == 'State[Inactive]' and
                s.no_of_running_instances == '0'
        ), snapshots))

    @classmethod
    def parse_output(cls, output: str) -> list:
        """Output parser"""

        # todo check what is returned if snapshot list is empty
        snapshots = output.split('List of Snapshots:\n')[1].split('\n\n')
        results = []
        if snapshots:

            for snapshot in snapshots:
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

        def __str__(self) -> str:
            return str(vars(self))


if __name__ == '__main__':
    pass
