from unittest import TestCase, main
from bpmtoolbox.bpm import BPMTool


class BPM(TestCase):
    def setUp(self) -> None:
        self.BPMTool = BPMTool()

        # BPMShowProcessApplication output, see https://www.ibm.com/docs/en/baw/19.x?topic=scripting-bpmshowprocessapplication
        self.output_2_snapshots = """Name: Credit Card Dispute Management
Acronym: CCDMDIP
Description: Main Process Application of the Credit Card Dispute Management Application.


Contains:

- the Manage Dispute Case type
- the related Launch UI
- related Activities
Toolkit: false
Tracks:

Track Name: Main
Track Acronym: Main
Default: true

Tip:
Created On: 2014-05-13 11:21:30.289
Created By: User.1
State: State[Inactive]
Capability: Capability[Standard]
No of running instances: 0

List of Snapshots:
Name: sn_for_Hursley
Acronym: SFH
Created On: 2014-05-12 14:05:08.563
Created By: User.9
Is Default: false
State: State[Inactive]
Capability: Capability[Standard]
No of running instances: 0

Name: ws_changed_smtpServer2
Acronym: WCSS2
Created On: 2014-05-13 11:21:30.289
Created By: User.1
Is Default: false
State: State[Inactive]
Capability: Capability[Standard]
No of running instances: 1

Name: ws_changed_smtpServer2
Acronym: WCSS2
Created On: 2014-05-13 11:21:30.289
Created By: User.1
Is Default: false
State: State[Active]
Capability: Capability[Standard]
No of running instances: 0"""

    def test_parse_output(self):
        results = self.BPMTool.parse_output(self.output_2_snapshots)
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0].name, 'sn_for_Hursley')

    def test_get_snapshots_to_clean(self):
        results = self.BPMTool.parse_output(self.output_2_snapshots)
        filtered_results = self.BPMTool.get_snapshots_to_clean(results)
        self.assertEqual(len(filtered_results), 1)


if __name__ == '__main__':
    main()
