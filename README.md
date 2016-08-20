[![Build Status](https://travis-ci.org/eon01/DoMonit.svg?branch=master)](https://travis-ci.org/eon01/DoMonit)
# DoMonit

A deadly simple monitoring tool for Docker - Using A Python Wrapper For Docker API.
[The Blog Post](https://medium.com/@eon01/monitoring-docker-with-python-domonit-34440b8c6830)

# Compatibility

A Python wrapper for Dokcer API 1.24 compatible with Docker 1.12.x and later.

# Purpose 

The purpose is to write python scripts easily for monitoring all of your Docker containers (running in a Linux distibution - other OS are coming soon in the roadmap of development).

# The Wrapper

This is the Alpha, moving to Beta very very soon :-)

The wrapper contains these classes:

```
api/
├── changes.py
├── containers.py
├── errors.py
├── ids.py
├── inspect.py
├── logs.py
├── process.py
└── stats.py
```

Where :

**Containers** : List containers

**Inspect** : Return low-level information on the container id

**Ids** : Return containers IDs

**Logs** : Get stdout and stderr logs from the container id

**Process** : List processes running inside the container id. On Unix systems this is done by running the ps command. This endpoint is not supported on Windows.

**Stats** : This endpoint returns a live stream of a container’s resource usage statistics.

# Using virtualenv:

```
virtualenv DoMonit
cd DoMonit 
git clone https://github.com/eon01/DoMonit.git
. bin/activate
cd DoMonit
pip install -r requirements.txt
#To Test:
python examples.py
```
# Example

Create a virtual environement 
```
virtualenv domonit
cd domonit 
. bin/activate
git clone https://github.com/eon01/DoMonit.git
cd DoMonit
pip install -r requirements.txt
python examples.py
```

# Example

This is an example script:

```
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
```

For the following 5 running containers:

```
docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
1a29e9652822        instavote/vote      "gunicorn app:app -b "   12 seconds ago      Up 11 seconds       80/tcp, 100/tcp     vote_webapp_3
6ca598188d1a        instavote/vote      "gunicorn app:app -b "   12 seconds ago      Up 11 seconds       80/tcp, 100/tcp     vote_webapp_4
7f1a6bfaf95b        instavote/vote      "gunicorn app:app -b "   12 seconds ago      Up 11 seconds       80/tcp, 100/tcp     vote_webapp_5
e3a7066ba953        instavote/vote      "gunicorn app:app -b "   6 days ago          Up 5 hours          80/tcp, 100/tcp     vote_webapp_2
1e557c8dc5f7        instavote/vote      "gunicorn app:app -b "   6 days ago          Up 5 hours          80/tcp, 100/tcp     vote_webapp_1
```

the execution result of the example above is:


```
Number of containers is : 5 

#Container name
/vote_webapp_3

#Container id
1a29e9652822447a440799306f4edb65003bca9cdea4c56e1e0ba349d5112d3e

#Memory usage %
0.697797903077

#The number of times that a process of the cgroup triggered a major fault
15

#Same output as ps aux in *nix
{u'Processes': [[u'root', u'26636', u'0.0', u'0.2', u'76808', u'16228', u'?', u'Ss', u'15:43', u'0:00', u'/usr/local/bin/python2 /usr/local/bin/gunicorn app:app -b 0.0.0.0:80 --log-file - --access-logfile - --workers 4 --keep-alive 0'], [u'root', u'26773', u'0.0', u'0.2', u'88776', u'19976', u'?', u'S', u'15:43', u'0:00', u'/usr/local/bin/python2 /usr/local/bin/gunicorn app:app -b 0.0.0.0:80 --log-file - --access-logfile - --workers 4 --keep-alive 0'], [u'root', u'26784', u'0.0', u'0.2', u'88572', u'19800', u'?', u'S', u'15:43', u'0:00', u'/usr/local/bin/python2 /usr/local/bin/gunicorn app:app -b 0.0.0.0:80 --log-file - --access-logfile - --workers 4 --keep-alive 0'], [u'root', u'26787', u'0.0', u'0.2', u'88568', u'19816', u'?', u'S', u'15:43', u'0:00', u'/usr/local/bin/python2 /usr/local/bin/gunicorn app:app -b 0.0.0.0:80 --log-file - --access-logfile - --workers 4 --keep-alive 0'], [u'root', u'26793', u'0.0', u'0.2', u'88572', u'19828', u'?', u'S', u'15:43', u'0:00', u'/usr/local/bin/python2 /usr/local/bin/gunicorn app:app -b 0.0.0.0:80 --log-file - --access-logfile - --workers 4 --keep-alive 0']], u'Titles': [u'USER', u'PID', u'%CPU', u'%MEM', u'VSZ', u'RSS', u'TTY', u'STAT', u'START', u'TIME', u'COMMAND']}

...etc
```

# ToDo
- Documentation
- Exception & timeout handling
