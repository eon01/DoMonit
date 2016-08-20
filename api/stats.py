import requests_unixsocket
import json

from lib.utils import Utils


u = Utils()


#https://docs.docker.com/engine/reference/api/docker_remote_api_v1.24/
class Stats():


    def __init__(self, container_id, stream = "0"):
        
        self.container_id = container_id
        self.stream = stream

        self.base = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
        self.url = "/containers/%s/stats?stream=%s" % (self.container_id, self.stream)
        
        self.session = requests_unixsocket.Session()
        try:
            self.resp = self.session.get( self.base + self.url)
        except Exception as ex:
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print message 



    def stats(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return ('{}'.format( respj))            
            
    def read(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          
        respj = self.resp.json()      
        return ('{}'.format( respj["read"]) )
        return "test"

    def pids_stats_current(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          
        respj = self.resp.json()      
        return ('{}'.format( respj["pids_stats"]["current"]) )

    #for multi networking inside a container : https://github.com/docker/docker/issues/17750
    def networks(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          
        respj = self.resp.json()      
        return ('{}'.format( respj["networks"]  ) )

    def interfaces(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          
        respj = self.resp.json()      
        return ('{}'.format( respj["networks"].keys()   ) )

    def rx_bytes(self, interface):
        resp = self.resp
        self.interface = interface
        if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
        elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))          
        respj = self.resp.json()      
        return ('{}'.format( respj["networks"][interface]["rx_bytes"] ) )

    def rx_dropped(self, interface):
        resp = self.resp
        self.interface = interface
        if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
        elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))          
        respj = self.resp.json()      
        return ('{}'.format( respj["networks"][interface]["rx_dropped"] ) )

    def rx_errors(self, interface):
        resp = self.resp
        self.interface = interface
        if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
        elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))          
        respj = self.resp.json()      
        return ('{}'.format( respj["networks"][interface]["rx_errors"] ) )

    def rx_packets(self, interface):
        resp = self.resp
        self.interface = interface
        if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
        elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))          
        respj = self.resp.json()      
        return ('{}'.format( respj["networks"][interface]["rx_packets"] ) )

    def tx_bytes(self, interface):
        resp = self.resp
        self.interface = interface
        if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
        elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))          
        respj = self.resp.json()      
        return ('{}'.format( respj["networks"][interface]["tx_bytes"] ) )

    def tx_dropped(self, interface):
        resp = self.resp
        self.interface = interface
        if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
        elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))          
        respj = self.resp.json()      
        return ('{}'.format( respj["networks"][interface]["tx_dropped"] ) )

    def tx_errors(self, interface):
        resp = self.resp
        self.interface = interface
        if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
        elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))          
        respj = self.resp.json()      
        return ('{}'.format( respj["networks"][interface]["tx_errors"] ) )

    def tx_packets(self, interface):
        resp = self.resp
        self.interface = interface
        if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
        elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))          
        respj = self.resp.json()      
        return ('{}'.format( respj["networks"][interface]["tx_packets"] ) )

# Memory Stats

    def memory_stats(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"] ) )

    def unevictable(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["unevictable"] ) )

    def total_inactive_file(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_inactive_file"] ) )

    def total_rss_huge(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_rss_huge"] ) )

    def writeback(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["writeback"] ) )

    def total_cache(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_cache"] ) )

    def total_mapped_file(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_mapped_file"] ) )

    def mapped_file(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["mapped_file"] ) )

    def pgfault(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["pgfault"] ) )

    def total_writeback(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_writeback"] ) )

    def hierarchical_memory_limit(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["hierarchical_memory_limit"] ) )

    def total_active_file(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_active_file"] ) )

    def rss_huge(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["rss_huge"] ) )

    def cache(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["cache"] ) )

    def active_anon(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["active_anon"] ) )

    def pgmajfault(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["pgmajfault"] ) )

    def total_pgpgout(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_pgpgout"] ) )

    def pgpgout(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["pgpgout"] ) )

    def total_active_anon(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_active_anon"] ) )

    def total_unevictable(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_unevictable"] ) )

    def total_pgfault(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_pgfault"] ) )

    def total_pgmajfault(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_pgmajfault"] ) )

    def total_inactive_anon(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_inactive_anon"] ) )

    def total_unevictable(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_unevictable"] ) )

    def total_pgfault(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_pgfault"] ) )

    def total_pgmajfault(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_pgmajfault"] ) )

    def total_inactive_anon(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_inactive_anon"] ) )

    def inactive_file(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["inactive_file"] ) )

    def pgpgin(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["pgpgin"] ) )

    def total_pgpgin(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_pgpgin"] ) )

    def rss(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["rss"] ) )

    def active_file(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["active_file"] ) )

    def inactive_anon(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["inactive_anon"] ) )

    def total_rss(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["stats"]["total_rss"] ) )

    def max_usage(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["max_usage"] ) )

    def usage(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["usage"] ) )

    def failcnt(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["failcnt"] ) )

    def limit(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["memory_stats"]["limit"] ) )

    # blkio_stats ToDo: io_service_time_recursive sectors_recursive io_service_bytes_recursive io_time_recursive io_queue_recursive io_merged_recursive io_wait_time_recursive

    def blkio_stats(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["blkio_stats"] ) )

    # CPU

    # CPU
    def cpu_stats_cpu_stats(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["cpu_stats"] ) )

    def cpu_stats_usage_in_usermode(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["cpu_stats"]["cpu_usage"]["usage_in_usermode"] ) )

    def cpu_stats_total_usage(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["cpu_stats"]["cpu_usage"]["total_usage"] ) )

    def cpu_stats_percpu_usage(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["cpu_stats"]["cpu_usage"]["percpu_usage"] ) )

    def cpu_stats_usage_in_kernelmode(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["cpu_stats"]["cpu_usage"]["usage_in_kernelmode"] ) )

    def cpu_stats_system_cpu_usage(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["cpu_stats"]["system_cpu_usage"] ) )

    def cpu_stats_throttling_data(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["cpu_stats"]["throttling_data"] ) )

    def cpu_stats_period(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["cpu_stats"]["throttling_data"]["periods"] ) )

    def cpu_stats_throttled_periods(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["cpu_stats"]["throttling_data"]["throttled_periods"] ) )

    def cpu_stats_throttled_time(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["cpu_stats"]["throttling_data"]["throttled_time"] ) )


    # Per CPU
    def percpu_stats(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["precpu_stats"] ) )

    def percpu_usage_in_usermode(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["percpu_stats"]["cpu_usage"]["usage_in_usermode"] ) )

    def percpu_total_usage(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["percpu_stats"]["cpu_usage"]["total_usage"] ) )

    def percpu_percpu_usage(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["percpu_stats"]["cpu_usage"]["percpu_usage"] ) )

    def percpu_usage_in_kernelmode(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["percpu_stats"]["cpu_usage"]["usage_in_kernelmode"] ) )

    def percpu_system_cpu_usage(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["percpu_stats"]["system_cpu_usage"] ) )

    def percpu_throttling_data(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["percpu_stats"]["throttling_data"] ) )

    def percpu_period(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["percpu_stats"]["throttling_data"]["periods"] ) )

    def percpu_throttled_periods(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["percpu_stats"]["throttling_data"]["throttled_periods"] ) )

    def percpu_throttled_time(self):
        resp = self.resp
        url = self.url
        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)

          

        respj = self.resp.json()
        return ('{}'.format( respj["percpu_stats"]["throttling_data"]["throttled_time"] ) )


