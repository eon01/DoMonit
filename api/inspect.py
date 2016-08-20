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

    def host_config_binds(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Binds"]) ) 

    def host_config_maximum_iops(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["MaximumIOps"]) ) 

    def host_config_maximum_iobps(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["MaximumIOBps"]) ) 

    def host_config_blkio_weight_device(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["BlkioWeightDevice"]) ) 

    def host_config_blkio_device_read_bps(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["BlkioDeviceReadBps"]) ) 

    def host_config_blkio_device_write_bps(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["BlkioDeviceWriteBps"]) ) 

    def host_config_blkio_device_write_iops(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["BlkioDeviceWriteIOps"]) ) 

    def host_config_cap_add(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CapAdd"]) ) 

    def host_config_cap_drop(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CapDrop"]) ) 

    def host_config_container_id_file(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["ContainerIDFile"]) ) 

    def host_config_cpuset_cpus(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CpusetCpus"]) ) 

    def host_config_cpuset_mems(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CpusetMems"]) ) 

    def host_config_cpu_percent(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CpuPercent"]) ) 

    def host_config_cpu_shares(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CpuShares"]) ) 

    def host_config_cpu_period(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["CpuPeriod"]) ) 

    def host_config_devices(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Devices"]) ) 

    def host_config_dns(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Dns"]) ) 

    def host_config_dns_options(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["DnsOptions"]) ) 

    def host_config_dns_search(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["DnsSearch"]) ) 

    def host_config_extra_hosts(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["ExtraHosts"]) ) 

    def host_config_ipc_mode(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["IpcMode"]) ) 

    def host_config_links(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Links"]) ) 

    def host_config_lxc_conf(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["LxcConf"]) ) 

    def host_config_memory(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Memory"]) ) 

    def host_config_memory_swap(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["DnsOptions"]) ) 

    def host_config_memory_reservation(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["MemoryReservation"]) ) 

    def host_config_kernel_memory(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["KernelMemory"]) ) 

    def host_config_oom_kill_disable(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["OomKillDisable"]) ) 

    def host_config_oom_score_adj(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["OomScoreAdj"]) ) 

    def host_config_network_mode(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["NetworkMode"]) ) 

    def host_config_pid_mode(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["PidMode"]) ) 

    def host_config_port_bindings(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["PortBindings"]) ) 

    def host_config_privileged(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Privileged"]) )

    def host_config_readonly_rootfs(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["ReadonlyRootfs"]) ) 

    def host_config_publish_all_ports(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["PublishAllPorts"]) ) 

    def host_config_restart_policy_maximum_retry_count(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["RestartPolicy"]["MaximumRetryCount"]) ) 

    def host_config_restart_policy_name(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["RestartPolicy"]["Name"]) ) 

    def host_config_log_config_config(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["LogConfig"]["Config"]) ) 

    def host_config_log_config_type(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["LogConfig"]["Type"]) ) 

    def host_config_security_opt(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["SecurityOpt"]) ) 

    def host_config_sysctls(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Sysctls"]) ) 

    def host_config_storage_opt(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["StorageOpt"]) ) 

    def host_config_volumes_from(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["VolumesFrom"]) ) 

    def host_config_ulimits(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["Ulimits"]) ) 

    def host_config_volume_driver(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["VolumeDriver"]) ) 

    def host_config_volume_driver(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["VolumeDriver"]) ) 

    def host_config_host_config_shm_size(self):
        resp = self.resp
        url = self.url

        resp_status_code = resp.status_code
        u.check_resp(resp_status_code, url)
          
        respj = self.resp.json()      
        return( '{}'.format( respj["HostConfig"]["ShmSize"]) ) 

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
