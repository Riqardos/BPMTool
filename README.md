# BPMTool

### Prerequisites
- AdminTask

### Install
`pip install git+https://github.com/Riqardos/BPMTool.git`

### Usage
```python
from bpmtoolbox.bpm import BPMTool
bpm_tool = BPMTool('acronymID')

snapshots = bpm_tool.get_all_snapshots() # -> [<bpmtoolbox.bpm.BPMTool.SnapShot object at 0x0000028D527ACF10>, ...]
print(snapshots[0].name) # -> sn_for_Hursley

bpm_tool.clean_snapshots()
```

### Tests
To run test, go to the root directory and run: `python -m unittest`
