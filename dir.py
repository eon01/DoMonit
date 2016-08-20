#!/usr/bin/env python
from __future__ import division

from api.containers import Containers
from api.ids import Ids
from api.inspect import Inspect
from api.logs import Logs
from api.process import Process
from api.changes import Changes
from api.stats import Stats


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
