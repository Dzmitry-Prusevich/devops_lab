#!/usr/bin/env python
from snap import snap

try:
    snap.write_info()
except KeyError:
    print("Place config.ini in current directory with next options:\n\n"
          "[common]\n\n"
          "output = json\n"
          "interval = 5\n\n"
          "where output - type of file,\n"
          "and interval - time in minutes between taking snapshots")
except KeyboardInterrupt:
    print("Snapshot stops its work")
