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
i = Ids()

print ("Number of containers is : %s " % (sum(1 for i in i.ids())))

if __name__ == "__main__":

    for c_id in i.ids():

        ins = Inspect(c_id)
        sta = Stats(c_id)
        proc = Process(c_id, ps_args = "aux")



        # Container name
        print ("\n#Container name")
        print ins.name()
 
        # Container id
        print ("\n#Container id")
        print ins.id()

        # Memory usage
        mem_u = sta.usage()

        # Memory limit
        mem_l = sta.limit()

        # Memory usage %
        print ("\n#Memory usage %")
        print  int(mem_u)*100/int(mem_l)


        # The number of times that a process of the cgroup triggered a "major fault"
        print ("\n#The number of times that a process of the cgroup triggered a major fault")
        print sta.pgmajfault()
  

        # Same output as ps aux in *nix
        print("\n#Same output as ps aux in *nix")
        print proc.ps()



