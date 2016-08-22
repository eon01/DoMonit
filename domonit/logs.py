#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests_unixsocket
from errors import NoSuchContainerError, ServerErrorError

from utils.utils import Utils
u = Utils()



#https://docs.docker.com/engine/reference/api/docker_remote_api_v1.24/
class Logs():

    def __init__(self, container_id, *args, **kwargs ):

        self.container_id = container_id
        self.stderr = kwargs.get("stderr", "true")
        self.stdout = kwargs.get("stdout", "true")
        self.timestamps = kwargs.get("timestamps", "false")
        self.follow = kwargs.get("follow", "false")
        self.tail = kwargs.get("tail", "all")
        self.since = kwargs.get("since", "0")
        self.details = kwargs.get("details", "false")
        
        self.base = "http+unix://%2Fvar%2Frun%2Fdocker.sock"

        self.url = (
	      "/containers/%s/logs?"\
              "stderr=%s"\
              "&stdout=%s"\
              "&timestamps=%s"\
              "&follow=%s"\
              "&tail=%s"\
              "&since=%s"\
              "&details=%s"
        )%(
              self.container_id, 
              self.stderr, 
              self.stdout, 
              self.timestamps, 
              self.follow, 
              self.tail, 
              self.since, 
              self.details 
           )

        self.session = requests_unixsocket.Session()
        self.resp = self.session.get( self.base + self.url)


    def logs(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)          

        #respj = self.resp.json()      
        return('{}'.format( resp.text ) )
