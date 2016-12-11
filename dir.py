#!/usr/bin/env python
from __future__ import division

from domonit.containers import Containers
from domonit.ids import Ids
from domonit.inspect import Inspect
from domonit.logs import Logs
from domonit.process import Process
from domonit.changes import Changes
from domonit.stats import Stats
from domonit.events import Events


import json


c = Containers()
print("Containers()")
print dir(c)
print("\n")


i = Ids()
print("Ids()")
print dir(i)
print("\n")

if __name__ == "__main__":

    for c_id in i.ids():

        ins = Inspect(c_id)
        print("Inspect()")
        print dir(ins)
	print("\n")

        sta = Stats(c_id)
        print("Stats()")
        print dir(sta)
	print("\n")

        proc = Process(c_id, ps_args = "aux")
        print("Process()")
        print dir(proc)
	print("\n")

        log = Logs(c_id)
        print("Logs()")
        print dir(log)
	print("\n")

        cha = Changes(c_id)
        print("Changes()")
        print dir(cha)
	print("\n")

eve = Events()
print("Events()")
print dir(eve)
print("\n")
