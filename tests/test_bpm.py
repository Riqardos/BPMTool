from unittest import TestCase, main
from bpmtoolbox.bpm import BPMApp
import io, sys

class BPM(TestCase):
    def setUp(self) -> None:
        self.BPMTool = BPMApp("test_acronym")
        
        # BPMShowProcessApplication output, see https://www.ibm.com/docs/en/baw/19.x?topic=scripting-bpmshowprocessapplication
        self.output_BPMShowProcessApplication = """Name: KDEV Dokument\nAcronym: KDEV01\nDescription: null\nToolkit: false\nTracks:\n\n\tList of Snapshots: \n\t\tName: 210331_0906 KDEV01\n\t\tAcronym: 2103310\n\t\tCreated On: 2021-03-31 09:11:15.694\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210422_1306 KDEV01\n\t\tAcronym: 2104221\n\t\tCreated On: 2021-04-22 13:09:14.747\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210421_1616 KDEV01\n\t\tAcronym: 21042_3\n\t\tCreated On: 2021-04-21 16:30:14.695\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210422_1352 KDEV01\n\t\tAcronym: 21042_5\n\t\tCreated On: 2021-04-22 13:56:28.059\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210421_1743 KDEV01\n\t\tAcronym: 21042_4\n\t\tCreated On: 2021-04-21 17:48:28.925\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210423_0938 KDEV01\n\t\tAcronym: 2104230\n\t\tCreated On: 2021-04-23 09:41:24.245\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210616_1153 KDEV01\n\t\tAcronym: 2106161\n\t\tCreated On: 2021-06-16 17:03:10.483\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210526_0809 KDEV01\n\t\tAcronym: 2105260\n\t\tCreated On: 2021-05-26 08:37:12.125\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210526_0957 KDEV01\n\t\tAcronym: 21052_1\n\t\tCreated On: 2021-05-26 10:01:56.832\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210527_1400 KDEV01\n\t\tAcronym: 2105271\n\t\tCreated On: 2021-05-27 14:03:47.562\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 201028_1507 KDEV01\n\t\tAcronym: 2010281\n\t\tCreated On: 2021-08-17 10:10:14.127\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210819_1342 KDEV01\n\t\tAcronym: 21081_3\n\t\tCreated On: 2021-08-19 13:44:44.241\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210817_1012 KDEV01\n\t\tAcronym: 2108171\n\t\tCreated On: 2021-08-17 10:27:38.52\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 201104_1505 KDEV01\n\t\tAcronym: 2011041\n\t\tCreated On: 2021-08-17 10:47:50.246\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210817_1046 KDEV01\n\t\tAcronym: 21081_1\n\t\tCreated On: 2021-08-17 10:53:08.033\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 201118_1615 KDEV01\n\t\tAcronym: 2011181\n\t\tCreated On: 2021-08-17 11:37:42.034\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210817_1050 KDEV01\n\t\tAcronym: 21081_2\n\t\tCreated On: 2021-08-17 11:40:46.465\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210819_1117 KDEV01\n\t\tAcronym: 2108191\n\t\tCreated On: 2021-08-19 11:22:51.402\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210831_1116 KDEV01\n\t\tAcronym: 2108311\n\t\tCreated On: 2021-08-31 11:20:22.437\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210903_0945 KDEV01\n\t\tAcronym: 2109030\n\t\tCreated On: 2021-09-03 09:50:12.614\n\t\tCreated By: User.9\n\t\tIs Default: false\n\t\tState: State[Inactive]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 0\n\n\t\tName: 210903_1022 KDEV01\n\t\tAcronym: 2109031\n\t\tCreated On: 2021-09-03 10:25:32.729\n\t\tCreated By: User.9\n\t\tIs Default: true\n\t\tState: State[Active]\n\t\tCapability: Capability[Standard]\n\t\tNo of running instances: 199\n\n"""
        
        #monkey patch
        def raise_(ex):
            raise ex

        self.BPMTool.get_all_snapshots_from_bpm = lambda: self.output_BPMShowProcessApplication
        self.BPMTool.delete_snapshot_from_bpm = lambda snapshot: True if snapshot.acronym != '2103310' else raise_(Exception('Delete error'))

    class CapturingStdout(list):
        def __enter__(self):
            self._stdout = sys.stdout
            sys.stdout = self._stringio = io.StringIO()
            return self
        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            del self._stringio    # free up some memory
            sys.stdout = self._stdout

    def test_parse_output(self):
        results = self.BPMTool.parse_bpm_output(self.output_BPMShowProcessApplication)
        self.assertEqual(len(results), 21)
        self.assertEqual(results[0].name, '210331_0906 KDEV01')

    def test_get_snapshots_to_clean(self):
        results = self.BPMTool.parse_bpm_output(self.output_BPMShowProcessApplication)
        filtered_results = self.BPMTool.filter_snapshots(results)
        self.assertEqual(len(filtered_results), 20)

    def test_generate_stats(self):
        snapshots = self.BPMTool.parse_bpm_output(self.output_BPMShowProcessApplication)
        stat_dict = self.BPMTool.generate_stats(snapshots)
        self.assertEqual(stat_dict['State[Inactive]'], 20)
        self.assertEqual(stat_dict['State[Active]'], 1)
    
    def test_get_snapshots_stat(self):
        with self.CapturingStdout() as stdout:
            self.BPMTool.get_snapshots_stat()
        self.assertEqual(stdout[1], "Active: 1; [('2109031', '199')]")

    def test_get_all_snapshots_formatted(self):
        with self.CapturingStdout() as stdout:
            self.BPMTool.get_all_snapshots_formatted()
        self.assertEqual(stdout[2:6], ['AcronymId: 2103310', 'State: State[Inactive]', 'Default: false', 'Number of instances: 0'])
    
    def test_clean_snapshots(self):
        with self.CapturingStdout() as stdout:
            self.BPMTool.clean_snapshots()
        self.assertEqual(stdout[-2:],['Deleted: 19', 'Skipped: 1'])


if __name__ == '__main__':
    main()
