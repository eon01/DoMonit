import requests_unixsocket
import json
from errors import BadParameterError, ServerErrorError

from lib.utils import Utils
u = Utils()


#https://docs.docker.com/engine/reference/api/docker_remote_api_v1.24/
class Containers():

    def __init__(self):        
        self.base = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
        self.url = "/containers/json"
        
        self.session = requests_unixsocket.Session()
        try:
            self.resp = self.session.get( self.base + self.url)
        except Exception as ex:
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print message

    def containers(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)       
        return json.loads(json.dumps(resp.json()))

    def names(self, c_id):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)       
        for item in resp.json():
            return('[{}]'.format(item["Names"]))

    def status(self, c_id):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)       
        for item in resp.json():
            return('{}'.format(item["Status"]))
  
    def created(self, c_id):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)       
        for item in resp.json():
            return('{}'.format(item["Created"]))

    def image(self, c_id):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)       
        for item in resp.json():
            return('{}'.format(item["Image"]))

    def labels(self, c_id):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)       
        for item in resp.json():
            return('[{}]'.format(item["Labels"]))

    def ports(self, c_id):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)       
        for item in resp.json():
            return('[{}]'.format(item["Ports"]))


    def host_config(self, c_id):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)       
        for item in resp.json():
            return('[{}]'.format(item["HostConfig"]))

    def network_settings(self, c_id):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)       
        for item in resp.json():
            return('[{}]'.format(item["NetworkSettings"]))

    def image_id(self, c_id):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)       
        for item in resp.json():
            return('{}'.format(item["ImageId"]))

    def command(self, c_id):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)       
        for item in resp.json():
            return('{}'.format(item["Command"]))

    def mounts(self, c_id):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)       
        for item in resp.json():
            return('[{}]'.format(item["Mounts"]))






