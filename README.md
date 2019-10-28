# How to use program

####installing 
_run 
pip install snapshot
_in the directory, where snapshot-1-py3-none-any.whl is placed
####run the program 
_place config.ini in dir where you want to run the program with next content:
[common]
output = json
interval = 1 
_after that run the program using command:
snapshot.py
####add module to your new python project
__run python
__add
from snap import snap
__running module
snap.write_info()
####uninstalling 
pip uninstall snapshot

