# BPMTool

## Prerequisites
- AdminTask api installed

## Install
`pip install git+https://github.com/Riqardos/BPMTool.git`

## Usage

### As module
```python
from bpmtoolbox.bpm import BPMApp

bpm_tool = BPMApp('acronymID')

snapshots = bpm_tool.get_all_snapshots()  # -> [<bpmtoolbox.bpm.BPMTool.SnapShot object at 0x0000028D527ACF10>, ...]
print(snapshots[0].name)  # -> sn_for_Hursley

bpm_tool.clean_snapshots()
```

### As script
`> python bpm.py acronymID -l`


#### Help:
```bash
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
```

## Tests
To run test, go to the root directory and run: `python -m unittest`
