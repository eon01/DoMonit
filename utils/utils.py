from domonit.errors import NoSuchContainerError, ServerErrorError, BadParameterError

class Utils():
   

    def __init__(self):
        pass   

    def check_resp(self, resp_status_code, url):
        self.resp_status_code = resp_status_code
        self.url = url

        if resp_status_code == 404:
            raise NoSuchContainerError('GET ' + url + ' {} '.format(resp_status_code)) 
        elif resp_status_code == 500:
            raise ServerErrorError('GET ' + url + ' {} '.format(resp_status_code))
        elif resp_status_code == 400:
            raise BadParameterError('GET ' + url + ' {} '.format(resp_status_code))
