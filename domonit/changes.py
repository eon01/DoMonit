import requests_unixsocket
import json
from errors import NoSuchContainerError, ServerErrorError


from utils.utils import Utils
u = Utils()


#https://docs.docker.com/engine/reference/api/docker_remote_api_v1.24/
class Changes():


    def __init__(self, container_id):
        self.container_id = container_id
        
        self.base = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
        self.url = "/containers/%s/changes" % (self.container_id)
        
        self.session = requests_unixsocket.Session()
        try:
            self.resp = self.session.get( self.base + self.url)
        except Exception as ex:
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print message            
            


    def changes(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)          

        return self.resp.json()
