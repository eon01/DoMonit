#!/usr/bin/env python

from domonit.events import Events

# Events is a stream of json sent by Docker API. In the Events class, we are only streaming in the same way the Docker events like Docker API make it.

e = Events()
events = e.events()

for event in events:
    print event

