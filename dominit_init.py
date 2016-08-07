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


if __name__ == "__main__":

    for c_id in i.ids():
        ins = Inspect(c_id)
        sta = Stats(c_id)



        #container name
        print ins.name()
 
        #container id
        print ins.id()

        print ins.cpu_percent()
 
        #CPU usage %
        print sta.percpu_stats()

        # Meomry usage
        mem_u = sta.usage()

        # Memory limit
        mem_l = sta.limit()

        # Momory usage %
        print  int(mem_u)*100/int(mem_l)






        print "\n"
