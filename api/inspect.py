import requests_unixsocket
import json
from errors import NoSuchContainerError, ServerErrorError

from lib.utils import Utils
u = Utils()


#https://docs.docker.com/engine/reference/api/docker_remote_api_v1.24/
class Inspect():


    def __init__(self, container_id):
        self.container_id = container_id
        
        self.base = "http+unix://%2Fvar%2Frun%2Fdocker.sock"
        self.url = "/containers/%s/json" % (self.container_id)
        
        self.session = requests_unixsocket.Session()
        try:
            self.resp = self.session.get( self.base + self.url)
        except Exception as ex:
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print message            

    def inspect(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return('{}'.format( respj) ) 
            

    def args(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return('{}'.format( respj["Args"]) ) 

    def app_armor_profile(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["AppArmorProfile"]) ) 

    def attach_stderr(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["AttachStderr"]) ) 

    def attach_stdin(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["AttachStdin"]) ) 

    def cmd(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return('{}'.format( respj["Config"]["Cmd"]) ) 

    def domainname(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["Domainname"]) ) 

    def entrypoint(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["Entrypoint"]) ) 


    def env(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["Env"]) ) 


    def exposed_ports(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["ExposedPorts"]) ) 

    def hostname(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["Hostname"]) ) 

    def image(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["Image"]) ) 


    def labels(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["Labels"]) ) 

    def mac_address(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["MacAddress"]) ) 

    def network_disabled(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["NetworkDisabled"]) ) 

    def on_build(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["OnBuild"]) ) 

    def open_stdin(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["OpenStdin"]) ) 


    def stdin_once(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["StdinOnce"]) ) 

    def tty(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["Tty"]) ) 


    def user(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["User"]) ) 

    def volumes(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["Volumes"]) ) 

    def working_dir(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["WorkingDir"]) ) 

    def stop_signal(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Config"]["StopSignal"]) ) 

    def created(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Created"]) ) 

    def driver(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Driver"]) ) 

    def exec_ids(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["ExecIds"]) ) 

    def binds(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Binds"]) ) 

    def maximum_iops(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["MaximumIOps"]) ) 

    def maximum_iobps(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["MaximumIOBps"]) ) 

    def blkio_weight_device(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["BlkioWeightDevice"]) ) 

    def blkio_device_read_bps(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["BlkioDeviceReadBps"]) ) 

    def blkio_device_write_bps(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["BlkioDeviceWriteBps"]) ) 

    def blkio_device_write_iops(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["BlkioDeviceWriteIOps"]) ) 

    def cap_add(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CapAdd"]) ) 

    def cap_drop(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CapDrop"]) ) 

    def container_id_file(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["ContainerIDFile"]) ) 

    def cpuset_cpus(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CpusetCpus"]) ) 

    def cpuset_mems(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CpusetMems"]) ) 

    def cpu_percent(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CpuPercent"]) ) 

    def cpu_shares(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CpuShares"]) ) 

    def cpu_period(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CpuPeriod"]) ) 

    def devices(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Devices"]) ) 

    def dns(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Dns"]) ) 

    def dns_options(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["DnsOptions"]) ) 

    def dns_search(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["DnsSearch"]) ) 

    def extra_hosts(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["ExtraHosts"]) ) 

    def ipc_mode(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["IpcMode"]) ) 

    def links(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Links"]) ) 

    def lxc_conf(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["LxcConf"]) ) 

    def memory(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Memory"]) ) 

    def memory_swap(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["DnsOptions"]) ) 

    def memory_reservation(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["MemoryReservation"]) ) 

    def kernel_memory(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["KernelMemory"]) ) 

    def oom_kill_disable(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["OomKillDisable"]) ) 

    def oom_score_adj(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["OomScoreAdj"]) ) 

    def network_mode(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["NetworkMode"]) ) 

    def pid_mode(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["PidMode"]) ) 

    def port_bindings(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["PortBindings"]) ) 

    def privileged(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Privileged"]) )

    def readonly_rootfs(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["ReadonlyRootfs"]) ) 

    def publish_all_ports(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["PublishAllPorts"]) ) 

    def restart_policy_maximum_retry_count(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["RestartPolicy"]["MaximumRetryCount"]) ) 

    def restart_policy_name(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["RestartPolicy"]["Name"]) ) 

    def log_config_config(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["LogConfig"]["Config"]) ) 

    def log_config_type(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["LogConfig"]["Type"]) ) 

    def security_opt(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["SecurityOpt"]) ) 

    def sysctls(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Sysctls"]) ) 

    def storage_opt(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["StorageOpt"]) ) 

    def volumes_from(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["VolumesFrom"]) ) 

    def ulimits(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Ulimits"]) ) 

    def volume_driver(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["hostconfig"]["VolumeDriver"]) ) 

    def volume_driver(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["hostconfig"]["VolumeDriver"]) ) 

    def shm_size(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["hostconfig"]["ShmSize"]) ) 

    def hostname_path(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostnamePath"]) ) 

    def hosts_path(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostsPath"]) ) 

    def log_path(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["LogPath"]) ) 

    def id(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Id"]) ) 

    def image(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Image"]) ) 

    def mount_label(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["MountLabel"]) ) 

    def name(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Name"]) ) 

    def bridge(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["Bridge"]) ) 

    def sandbox_id(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["SandboxID"]) ) 

    def hairpin_mode(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["HairpinMode"]) ) 

    def link_local_ipv6_address(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["LinkLocalIPv6Address"]) ) 

    def link_local_ipv6_prefix_len(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["LinkLocalIPv6PrefixLen"]) ) 

    def ports(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["Ports"]) ) 

    def sandbox_key(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["SandboxKey"]) ) 

    def secondary_ip_addresses(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["SecondaryIPAddresses"]) ) 

    def secondary_ipv6_addresses(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["SecondaryIPv6Addresses"]) ) 

    def endpoint_id(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["EndpointID"]) ) 

    def gateway(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["Gateway"]) ) 

    def global_ipv6_address(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["GlobalIPv6Address"]) ) 

    def global_ipv6_prefixLen(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["GlobalIPv6PrefixLen"]) ) 

    def ip_address(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["IPAddress"]) ) 

    def ip_prefixLen(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["IPPrefixLen"]) ) 

    def ipv6_gateway(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["IPv6Gateway"]) ) 

    def mac_address(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["NetworkSettings"]["MacAddress"]) ) 

    def networks(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()
        return respj["NetworkSettings"]["Networks"]

    def path(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["Path"]) ) 

    def process_label(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["ProcessLabel"]) ) 

    def resolv_conf_path(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["ResolvConfPath"]) ) 

    def restart_count(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["RestartCount"]) ) 

    def error(self):
         resp = self.resp
         if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
         elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))        
         respj = self.resp.json()      
         return( '{}'.format( respj["State"]["Error"]) ) 

    def exit_code(self):
         resp = self.resp
         if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
         elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))        
         respj = self.resp.json()      
         return( '{}'.format( respj["State"]["ExitCode"]) ) 
 
    def finished_at(self):
         resp = self.resp
         if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
         elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))        
         respj = self.resp.json()      
         return( '{}'.format( respj["State"]["FinishedAt"]) ) 
 
    def oom_killed(self):
         resp = self.resp
         if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
         elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))        
         respj = self.resp.json()      
         return( '{}'.format( respj["State"]["OOMKilled"]) ) 
 
    def dead(self):
         resp = self.resp
         if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
         elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))        
         respj = self.resp.json()      
         return( '{}'.format( respj["State"]["Dead"]) ) 
 
    def paused(self):
         resp = self.resp
         if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
         elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))        
         respj = self.resp.json()      
         return( '{}'.format( respj["State"]["Paused"]) ) 
 
    def pid(self):
         resp = self.resp
         if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
         elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))        
         respj = self.resp.json()      
         return( '{}'.format( respj["State"]["Pid"]) ) 
 
    def restarting(self):
         resp = self.resp
         if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
         elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))        
         respj = self.resp.json()      
         return( '{}'.format( respj["State"]["Restarting"]) ) 
 
    def running(self):
         resp = self.resp
         if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
         elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))        
         respj = self.resp.json()      
         return( '{}'.format( respj["State"]["Running"]) ) 
 
    def started_at(self):
         resp = self.resp
         if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
         elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))        
         respj = self.resp.json()      
         return( '{}'.format( respj["State"]["StartedAt"]) ) 
  
    def status(self):
         resp = self.resp
         if resp.status_code == 404:
            raise NoSuchContainerError('GET ' + self.url + ' {} '.format(resp.status_code)) 
         elif resp.status_code == 500:
            raise ServerErrorError('GET ' + self.url + ' {} '.format(resp.status_code))        
         respj = self.resp.json()      
         return( '{}'.format( respj["State"]["Status"]) ) 
 
    def mounts(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
            
        respj = self.resp.json()      
        return( '{}'.format( respj["Mounts"]) )
