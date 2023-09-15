from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportMetadata")


@_attrs_define
class ReportMetadata:
    """
    Example:
        {'docker_image_name_with_tag': 'docker_image_name_with_tag', 'kubernetes_ip': 'kubernetes_ip', 'public_ip':
            ['public_ip', 'public_ip'], 'kubernetes_cluster_name': 'kubernetes_cluster_name', 'docker_container_state':
            'docker_container_state', 'cpu_max': 6.027456183070403, 'pid': 7, 'kubernetes_created': 'kubernetes_created',
            'kubernetes_namespace': 'kubernetes_namespace', 'cmdline': 'cmdline', 'node_type': 'node_type',
            'interface_ip_map': 'interface_ip_map', 'pseudo': True, 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'kubernetes_cluster_id': 'kubernetes_cluster_id',
            'docker_container_networks': 'docker_container_networks', 'kubernetes_ports': ['kubernetes_ports',
            'kubernetes_ports'], 'version': 'version', 'pod_name': 'pod_name', 'ppid': 9, 'tags': ['tags', 'tags'],
            'docker_container_ports': 'docker_container_ports', 'kubernetes_is_in_host_network': True, 'instance_id':
            'instance_id', 'kernel_id': 'kernel_id', 'copy_of': 'copy_of', 'open_files': ['open_files', 'open_files'],
            'docker_env': 'docker_env', 'connection_count': 0, 'docker_image_size': 'docker_image_size', 'cpu_usage':
            1.4658129805029452, 'pod_id': 'pod_id', 'docker_label': 'docker_label', 'instance_type': 'instance_type',
            'docker_image_name': 'docker_image_name', 'user_defined_tags': ['user_defined_tags', 'user_defined_tags'],
            'local_networks': ['local_networks', 'local_networks'], 'cloud_region': 'cloud_region', 'kubernetes_state':
            'kubernetes_state', 'interface_names': ['interface_names', 'interface_names'], 'memory_usage': 5,
            'open_files_count': 2, 'kubernetes_public_ip': 'kubernetes_public_ip', 'private_ip': ['private_ip',
            'private_ip'], 'docker_container_network_mode': 'docker_container_network_mode', 'kubernetes_type':
            'kubernetes_type', 'resource_group': 'resource_group', 'docker_image_tag': 'docker_image_tag',
            'kubernetes_labels': 'kubernetes_labels', 'docker_container_ips': ['docker_container_ips',
            'docker_container_ips'], 'docker_image_id': 'docker_image_id', 'timestamp': 'timestamp', 'interface_ips':
            ['interface_ips', 'interface_ips'], 'availability_zone': 'availability_zone', 'is_console_vm': True, 'os': 'os',
            'local_cidr': ['local_cidr', 'local_cidr'], 'node_name': 'node_name', 'threads': 3, 'cloud_provider':
            'cloud_provider', 'docker_container_command': 'docker_container_command', 'agent_running': True, 'uptime': 2,
            'memory_max': 5, 'docker_image_created_at': 'docker_image_created_at', 'kernel_version': 'kernel_version',
            'docker_container_state_human': 'docker_container_state_human', 'docker_image_virtual_size':
            'docker_image_virtual_size', 'kubernetes_ingress_ip': ['kubernetes_ingress_ip', 'kubernetes_ingress_ip'],
            'host_name': 'host_name', 'node_id': 'node_id'}

    Attributes:
        agent_running (Union[Unset, bool]):
        availability_zone (Union[Unset, str]):
        cloud_provider (Union[Unset, str]):
        cloud_region (Union[Unset, str]):
        cmdline (Union[Unset, str]):
        connection_count (Union[Unset, int]):
        copy_of (Union[Unset, str]):
        cpu_max (Union[Unset, float]):
        cpu_usage (Union[Unset, float]):
        docker_container_command (Union[Unset, str]):
        docker_container_created (Union[Unset, str]):
        docker_container_ips (Union[Unset, List[str]]):
        docker_container_name (Union[Unset, str]):
        docker_container_network_mode (Union[Unset, str]):
        docker_container_networks (Union[Unset, str]):
        docker_container_ports (Union[Unset, str]):
        docker_container_state (Union[Unset, str]):
        docker_container_state_human (Union[Unset, str]):
        docker_env (Union[Unset, str]):
        docker_image_created_at (Union[Unset, str]):
        docker_image_id (Union[Unset, str]):
        docker_image_name (Union[Unset, str]):
        docker_image_name_with_tag (Union[Unset, str]):
        docker_image_size (Union[Unset, str]):
        docker_image_tag (Union[Unset, str]):
        docker_image_virtual_size (Union[Unset, str]):
        docker_label (Union[Unset, str]):
        host_name (Union[Unset, str]):
        instance_id (Union[Unset, str]):
        instance_type (Union[Unset, str]):
        interface_ip_map (Union[Unset, str]):
        interface_ips (Union[Unset, List[str]]):
        interface_names (Union[Unset, List[str]]):
        is_console_vm (Union[Unset, bool]):
        kernel_id (Union[Unset, str]):
        kernel_version (Union[Unset, str]):
        kubernetes_cluster_id (Union[Unset, str]):
        kubernetes_cluster_name (Union[Unset, str]):
        kubernetes_created (Union[Unset, str]):
        kubernetes_ingress_ip (Union[Unset, List[str]]):
        kubernetes_ip (Union[Unset, str]):
        kubernetes_is_in_host_network (Union[Unset, bool]):
        kubernetes_labels (Union[Unset, str]):
        kubernetes_namespace (Union[Unset, str]):
        kubernetes_ports (Union[Unset, List[str]]):
        kubernetes_public_ip (Union[Unset, str]):
        kubernetes_state (Union[Unset, str]):
        kubernetes_type (Union[Unset, str]):
        local_cidr (Union[Unset, List[str]]):
        local_networks (Union[Unset, List[str]]):
        memory_max (Union[Unset, int]):
        memory_usage (Union[Unset, int]):
        node_id (Union[Unset, str]):
        node_name (Union[Unset, str]):
        node_type (Union[Unset, str]):
        open_files (Union[Unset, List[str]]):
        open_files_count (Union[Unset, int]):
        os (Union[Unset, str]):
        pid (Union[Unset, int]):
        pod_id (Union[Unset, str]):
        pod_name (Union[Unset, str]):
        ppid (Union[Unset, int]):
        private_ip (Union[Unset, List[str]]):
        pseudo (Union[Unset, bool]):
        public_ip (Union[Unset, List[str]]):
        resource_group (Union[Unset, str]):
        tags (Union[Unset, List[str]]):
        threads (Union[Unset, int]):
        timestamp (Union[Unset, str]):
        uptime (Union[Unset, int]):
        user_defined_tags (Union[Unset, List[str]]):
        version (Union[Unset, str]):
    """

    agent_running: Union[Unset, bool] = UNSET
    availability_zone: Union[Unset, str] = UNSET
    cloud_provider: Union[Unset, str] = UNSET
    cloud_region: Union[Unset, str] = UNSET
    cmdline: Union[Unset, str] = UNSET
    connection_count: Union[Unset, int] = UNSET
    copy_of: Union[Unset, str] = UNSET
    cpu_max: Union[Unset, float] = UNSET
    cpu_usage: Union[Unset, float] = UNSET
    docker_container_command: Union[Unset, str] = UNSET
    docker_container_created: Union[Unset, str] = UNSET
    docker_container_ips: Union[Unset, List[str]] = UNSET
    docker_container_name: Union[Unset, str] = UNSET
    docker_container_network_mode: Union[Unset, str] = UNSET
    docker_container_networks: Union[Unset, str] = UNSET
    docker_container_ports: Union[Unset, str] = UNSET
    docker_container_state: Union[Unset, str] = UNSET
    docker_container_state_human: Union[Unset, str] = UNSET
    docker_env: Union[Unset, str] = UNSET
    docker_image_created_at: Union[Unset, str] = UNSET
    docker_image_id: Union[Unset, str] = UNSET
    docker_image_name: Union[Unset, str] = UNSET
    docker_image_name_with_tag: Union[Unset, str] = UNSET
    docker_image_size: Union[Unset, str] = UNSET
    docker_image_tag: Union[Unset, str] = UNSET
    docker_image_virtual_size: Union[Unset, str] = UNSET
    docker_label: Union[Unset, str] = UNSET
    host_name: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    instance_type: Union[Unset, str] = UNSET
    interface_ip_map: Union[Unset, str] = UNSET
    interface_ips: Union[Unset, List[str]] = UNSET
    interface_names: Union[Unset, List[str]] = UNSET
    is_console_vm: Union[Unset, bool] = UNSET
    kernel_id: Union[Unset, str] = UNSET
    kernel_version: Union[Unset, str] = UNSET
    kubernetes_cluster_id: Union[Unset, str] = UNSET
    kubernetes_cluster_name: Union[Unset, str] = UNSET
    kubernetes_created: Union[Unset, str] = UNSET
    kubernetes_ingress_ip: Union[Unset, List[str]] = UNSET
    kubernetes_ip: Union[Unset, str] = UNSET
    kubernetes_is_in_host_network: Union[Unset, bool] = UNSET
    kubernetes_labels: Union[Unset, str] = UNSET
    kubernetes_namespace: Union[Unset, str] = UNSET
    kubernetes_ports: Union[Unset, List[str]] = UNSET
    kubernetes_public_ip: Union[Unset, str] = UNSET
    kubernetes_state: Union[Unset, str] = UNSET
    kubernetes_type: Union[Unset, str] = UNSET
    local_cidr: Union[Unset, List[str]] = UNSET
    local_networks: Union[Unset, List[str]] = UNSET
    memory_max: Union[Unset, int] = UNSET
    memory_usage: Union[Unset, int] = UNSET
    node_id: Union[Unset, str] = UNSET
    node_name: Union[Unset, str] = UNSET
    node_type: Union[Unset, str] = UNSET
    open_files: Union[Unset, List[str]] = UNSET
    open_files_count: Union[Unset, int] = UNSET
    os: Union[Unset, str] = UNSET
    pid: Union[Unset, int] = UNSET
    pod_id: Union[Unset, str] = UNSET
    pod_name: Union[Unset, str] = UNSET
    ppid: Union[Unset, int] = UNSET
    private_ip: Union[Unset, List[str]] = UNSET
    pseudo: Union[Unset, bool] = UNSET
    public_ip: Union[Unset, List[str]] = UNSET
    resource_group: Union[Unset, str] = UNSET
    tags: Union[Unset, List[str]] = UNSET
    threads: Union[Unset, int] = UNSET
    timestamp: Union[Unset, str] = UNSET
    uptime: Union[Unset, int] = UNSET
    user_defined_tags: Union[Unset, List[str]] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_running = self.agent_running
        availability_zone = self.availability_zone
        cloud_provider = self.cloud_provider
        cloud_region = self.cloud_region
        cmdline = self.cmdline
        connection_count = self.connection_count
        copy_of = self.copy_of
        cpu_max = self.cpu_max
        cpu_usage = self.cpu_usage
        docker_container_command = self.docker_container_command
        docker_container_created = self.docker_container_created
        docker_container_ips: Union[Unset, List[str]] = UNSET
        if not isinstance(self.docker_container_ips, Unset):
            docker_container_ips = self.docker_container_ips

        docker_container_name = self.docker_container_name
        docker_container_network_mode = self.docker_container_network_mode
        docker_container_networks = self.docker_container_networks
        docker_container_ports = self.docker_container_ports
        docker_container_state = self.docker_container_state
        docker_container_state_human = self.docker_container_state_human
        docker_env = self.docker_env
        docker_image_created_at = self.docker_image_created_at
        docker_image_id = self.docker_image_id
        docker_image_name = self.docker_image_name
        docker_image_name_with_tag = self.docker_image_name_with_tag
        docker_image_size = self.docker_image_size
        docker_image_tag = self.docker_image_tag
        docker_image_virtual_size = self.docker_image_virtual_size
        docker_label = self.docker_label
        host_name = self.host_name
        instance_id = self.instance_id
        instance_type = self.instance_type
        interface_ip_map = self.interface_ip_map
        interface_ips: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interface_ips, Unset):
            interface_ips = self.interface_ips

        interface_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.interface_names, Unset):
            interface_names = self.interface_names

        is_console_vm = self.is_console_vm
        kernel_id = self.kernel_id
        kernel_version = self.kernel_version
        kubernetes_cluster_id = self.kubernetes_cluster_id
        kubernetes_cluster_name = self.kubernetes_cluster_name
        kubernetes_created = self.kubernetes_created
        kubernetes_ingress_ip: Union[Unset, List[str]] = UNSET
        if not isinstance(self.kubernetes_ingress_ip, Unset):
            kubernetes_ingress_ip = self.kubernetes_ingress_ip

        kubernetes_ip = self.kubernetes_ip
        kubernetes_is_in_host_network = self.kubernetes_is_in_host_network
        kubernetes_labels = self.kubernetes_labels
        kubernetes_namespace = self.kubernetes_namespace
        kubernetes_ports: Union[Unset, List[str]] = UNSET
        if not isinstance(self.kubernetes_ports, Unset):
            kubernetes_ports = self.kubernetes_ports

        kubernetes_public_ip = self.kubernetes_public_ip
        kubernetes_state = self.kubernetes_state
        kubernetes_type = self.kubernetes_type
        local_cidr: Union[Unset, List[str]] = UNSET
        if not isinstance(self.local_cidr, Unset):
            local_cidr = self.local_cidr

        local_networks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.local_networks, Unset):
            local_networks = self.local_networks

        memory_max = self.memory_max
        memory_usage = self.memory_usage
        node_id = self.node_id
        node_name = self.node_name
        node_type = self.node_type
        open_files: Union[Unset, List[str]] = UNSET
        if not isinstance(self.open_files, Unset):
            open_files = self.open_files

        open_files_count = self.open_files_count
        os = self.os
        pid = self.pid
        pod_id = self.pod_id
        pod_name = self.pod_name
        ppid = self.ppid
        private_ip: Union[Unset, List[str]] = UNSET
        if not isinstance(self.private_ip, Unset):
            private_ip = self.private_ip

        pseudo = self.pseudo
        public_ip: Union[Unset, List[str]] = UNSET
        if not isinstance(self.public_ip, Unset):
            public_ip = self.public_ip

        resource_group = self.resource_group
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        threads = self.threads
        timestamp = self.timestamp
        uptime = self.uptime
        user_defined_tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.user_defined_tags, Unset):
            user_defined_tags = self.user_defined_tags

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_running is not UNSET:
            field_dict["agent_running"] = agent_running
        if availability_zone is not UNSET:
            field_dict["availability_zone"] = availability_zone
        if cloud_provider is not UNSET:
            field_dict["cloud_provider"] = cloud_provider
        if cloud_region is not UNSET:
            field_dict["cloud_region"] = cloud_region
        if cmdline is not UNSET:
            field_dict["cmdline"] = cmdline
        if connection_count is not UNSET:
            field_dict["connection_count"] = connection_count
        if copy_of is not UNSET:
            field_dict["copy_of"] = copy_of
        if cpu_max is not UNSET:
            field_dict["cpu_max"] = cpu_max
        if cpu_usage is not UNSET:
            field_dict["cpu_usage"] = cpu_usage
        if docker_container_command is not UNSET:
            field_dict["docker_container_command"] = docker_container_command
        if docker_container_created is not UNSET:
            field_dict["docker_container_created"] = docker_container_created
        if docker_container_ips is not UNSET:
            field_dict["docker_container_ips"] = docker_container_ips
        if docker_container_name is not UNSET:
            field_dict["docker_container_name"] = docker_container_name
        if docker_container_network_mode is not UNSET:
            field_dict["docker_container_network_mode"] = docker_container_network_mode
        if docker_container_networks is not UNSET:
            field_dict["docker_container_networks"] = docker_container_networks
        if docker_container_ports is not UNSET:
            field_dict["docker_container_ports"] = docker_container_ports
        if docker_container_state is not UNSET:
            field_dict["docker_container_state"] = docker_container_state
        if docker_container_state_human is not UNSET:
            field_dict["docker_container_state_human"] = docker_container_state_human
        if docker_env is not UNSET:
            field_dict["docker_env"] = docker_env
        if docker_image_created_at is not UNSET:
            field_dict["docker_image_created_at"] = docker_image_created_at
        if docker_image_id is not UNSET:
            field_dict["docker_image_id"] = docker_image_id
        if docker_image_name is not UNSET:
            field_dict["docker_image_name"] = docker_image_name
        if docker_image_name_with_tag is not UNSET:
            field_dict["docker_image_name_with_tag"] = docker_image_name_with_tag
        if docker_image_size is not UNSET:
            field_dict["docker_image_size"] = docker_image_size
        if docker_image_tag is not UNSET:
            field_dict["docker_image_tag"] = docker_image_tag
        if docker_image_virtual_size is not UNSET:
            field_dict["docker_image_virtual_size"] = docker_image_virtual_size
        if docker_label is not UNSET:
            field_dict["docker_label"] = docker_label
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if instance_type is not UNSET:
            field_dict["instance_type"] = instance_type
        if interface_ip_map is not UNSET:
            field_dict["interface_ip_map"] = interface_ip_map
        if interface_ips is not UNSET:
            field_dict["interface_ips"] = interface_ips
        if interface_names is not UNSET:
            field_dict["interface_names"] = interface_names
        if is_console_vm is not UNSET:
            field_dict["is_console_vm"] = is_console_vm
        if kernel_id is not UNSET:
            field_dict["kernel_id"] = kernel_id
        if kernel_version is not UNSET:
            field_dict["kernel_version"] = kernel_version
        if kubernetes_cluster_id is not UNSET:
            field_dict["kubernetes_cluster_id"] = kubernetes_cluster_id
        if kubernetes_cluster_name is not UNSET:
            field_dict["kubernetes_cluster_name"] = kubernetes_cluster_name
        if kubernetes_created is not UNSET:
            field_dict["kubernetes_created"] = kubernetes_created
        if kubernetes_ingress_ip is not UNSET:
            field_dict["kubernetes_ingress_ip"] = kubernetes_ingress_ip
        if kubernetes_ip is not UNSET:
            field_dict["kubernetes_ip"] = kubernetes_ip
        if kubernetes_is_in_host_network is not UNSET:
            field_dict["kubernetes_is_in_host_network"] = kubernetes_is_in_host_network
        if kubernetes_labels is not UNSET:
            field_dict["kubernetes_labels"] = kubernetes_labels
        if kubernetes_namespace is not UNSET:
            field_dict["kubernetes_namespace"] = kubernetes_namespace
        if kubernetes_ports is not UNSET:
            field_dict["kubernetes_ports"] = kubernetes_ports
        if kubernetes_public_ip is not UNSET:
            field_dict["kubernetes_public_ip"] = kubernetes_public_ip
        if kubernetes_state is not UNSET:
            field_dict["kubernetes_state"] = kubernetes_state
        if kubernetes_type is not UNSET:
            field_dict["kubernetes_type"] = kubernetes_type
        if local_cidr is not UNSET:
            field_dict["local_cidr"] = local_cidr
        if local_networks is not UNSET:
            field_dict["local_networks"] = local_networks
        if memory_max is not UNSET:
            field_dict["memory_max"] = memory_max
        if memory_usage is not UNSET:
            field_dict["memory_usage"] = memory_usage
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if node_name is not UNSET:
            field_dict["node_name"] = node_name
        if node_type is not UNSET:
            field_dict["node_type"] = node_type
        if open_files is not UNSET:
            field_dict["open_files"] = open_files
        if open_files_count is not UNSET:
            field_dict["open_files_count"] = open_files_count
        if os is not UNSET:
            field_dict["os"] = os
        if pid is not UNSET:
            field_dict["pid"] = pid
        if pod_id is not UNSET:
            field_dict["pod_id"] = pod_id
        if pod_name is not UNSET:
            field_dict["pod_name"] = pod_name
        if ppid is not UNSET:
            field_dict["ppid"] = ppid
        if private_ip is not UNSET:
            field_dict["private_ip"] = private_ip
        if pseudo is not UNSET:
            field_dict["pseudo"] = pseudo
        if public_ip is not UNSET:
            field_dict["public_ip"] = public_ip
        if resource_group is not UNSET:
            field_dict["resource_group"] = resource_group
        if tags is not UNSET:
            field_dict["tags"] = tags
        if threads is not UNSET:
            field_dict["threads"] = threads
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if user_defined_tags is not UNSET:
            field_dict["user_defined_tags"] = user_defined_tags
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agent_running = d.pop("agent_running", UNSET)

        availability_zone = d.pop("availability_zone", UNSET)

        cloud_provider = d.pop("cloud_provider", UNSET)

        cloud_region = d.pop("cloud_region", UNSET)

        cmdline = d.pop("cmdline", UNSET)

        connection_count = d.pop("connection_count", UNSET)

        copy_of = d.pop("copy_of", UNSET)

        cpu_max = d.pop("cpu_max", UNSET)

        cpu_usage = d.pop("cpu_usage", UNSET)

        docker_container_command = d.pop("docker_container_command", UNSET)

        docker_container_created = d.pop("docker_container_created", UNSET)

        docker_container_ips = cast(List[str], d.pop("docker_container_ips", UNSET))

        docker_container_name = d.pop("docker_container_name", UNSET)

        docker_container_network_mode = d.pop("docker_container_network_mode", UNSET)

        docker_container_networks = d.pop("docker_container_networks", UNSET)

        docker_container_ports = d.pop("docker_container_ports", UNSET)

        docker_container_state = d.pop("docker_container_state", UNSET)

        docker_container_state_human = d.pop("docker_container_state_human", UNSET)

        docker_env = d.pop("docker_env", UNSET)

        docker_image_created_at = d.pop("docker_image_created_at", UNSET)

        docker_image_id = d.pop("docker_image_id", UNSET)

        docker_image_name = d.pop("docker_image_name", UNSET)

        docker_image_name_with_tag = d.pop("docker_image_name_with_tag", UNSET)

        docker_image_size = d.pop("docker_image_size", UNSET)

        docker_image_tag = d.pop("docker_image_tag", UNSET)

        docker_image_virtual_size = d.pop("docker_image_virtual_size", UNSET)

        docker_label = d.pop("docker_label", UNSET)

        host_name = d.pop("host_name", UNSET)

        instance_id = d.pop("instance_id", UNSET)

        instance_type = d.pop("instance_type", UNSET)

        interface_ip_map = d.pop("interface_ip_map", UNSET)

        interface_ips = cast(List[str], d.pop("interface_ips", UNSET))

        interface_names = cast(List[str], d.pop("interface_names", UNSET))

        is_console_vm = d.pop("is_console_vm", UNSET)

        kernel_id = d.pop("kernel_id", UNSET)

        kernel_version = d.pop("kernel_version", UNSET)

        kubernetes_cluster_id = d.pop("kubernetes_cluster_id", UNSET)

        kubernetes_cluster_name = d.pop("kubernetes_cluster_name", UNSET)

        kubernetes_created = d.pop("kubernetes_created", UNSET)

        kubernetes_ingress_ip = cast(List[str], d.pop("kubernetes_ingress_ip", UNSET))

        kubernetes_ip = d.pop("kubernetes_ip", UNSET)

        kubernetes_is_in_host_network = d.pop("kubernetes_is_in_host_network", UNSET)

        kubernetes_labels = d.pop("kubernetes_labels", UNSET)

        kubernetes_namespace = d.pop("kubernetes_namespace", UNSET)

        kubernetes_ports = cast(List[str], d.pop("kubernetes_ports", UNSET))

        kubernetes_public_ip = d.pop("kubernetes_public_ip", UNSET)

        kubernetes_state = d.pop("kubernetes_state", UNSET)

        kubernetes_type = d.pop("kubernetes_type", UNSET)

        local_cidr = cast(List[str], d.pop("local_cidr", UNSET))

        local_networks = cast(List[str], d.pop("local_networks", UNSET))

        memory_max = d.pop("memory_max", UNSET)

        memory_usage = d.pop("memory_usage", UNSET)

        node_id = d.pop("node_id", UNSET)

        node_name = d.pop("node_name", UNSET)

        node_type = d.pop("node_type", UNSET)

        open_files = cast(List[str], d.pop("open_files", UNSET))

        open_files_count = d.pop("open_files_count", UNSET)

        os = d.pop("os", UNSET)

        pid = d.pop("pid", UNSET)

        pod_id = d.pop("pod_id", UNSET)

        pod_name = d.pop("pod_name", UNSET)

        ppid = d.pop("ppid", UNSET)

        private_ip = cast(List[str], d.pop("private_ip", UNSET))

        pseudo = d.pop("pseudo", UNSET)

        public_ip = cast(List[str], d.pop("public_ip", UNSET))

        resource_group = d.pop("resource_group", UNSET)

        tags = cast(List[str], d.pop("tags", UNSET))

        threads = d.pop("threads", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        uptime = d.pop("uptime", UNSET)

        user_defined_tags = cast(List[str], d.pop("user_defined_tags", UNSET))

        version = d.pop("version", UNSET)

        report_metadata = cls(
            agent_running=agent_running,
            availability_zone=availability_zone,
            cloud_provider=cloud_provider,
            cloud_region=cloud_region,
            cmdline=cmdline,
            connection_count=connection_count,
            copy_of=copy_of,
            cpu_max=cpu_max,
            cpu_usage=cpu_usage,
            docker_container_command=docker_container_command,
            docker_container_created=docker_container_created,
            docker_container_ips=docker_container_ips,
            docker_container_name=docker_container_name,
            docker_container_network_mode=docker_container_network_mode,
            docker_container_networks=docker_container_networks,
            docker_container_ports=docker_container_ports,
            docker_container_state=docker_container_state,
            docker_container_state_human=docker_container_state_human,
            docker_env=docker_env,
            docker_image_created_at=docker_image_created_at,
            docker_image_id=docker_image_id,
            docker_image_name=docker_image_name,
            docker_image_name_with_tag=docker_image_name_with_tag,
            docker_image_size=docker_image_size,
            docker_image_tag=docker_image_tag,
            docker_image_virtual_size=docker_image_virtual_size,
            docker_label=docker_label,
            host_name=host_name,
            instance_id=instance_id,
            instance_type=instance_type,
            interface_ip_map=interface_ip_map,
            interface_ips=interface_ips,
            interface_names=interface_names,
            is_console_vm=is_console_vm,
            kernel_id=kernel_id,
            kernel_version=kernel_version,
            kubernetes_cluster_id=kubernetes_cluster_id,
            kubernetes_cluster_name=kubernetes_cluster_name,
            kubernetes_created=kubernetes_created,
            kubernetes_ingress_ip=kubernetes_ingress_ip,
            kubernetes_ip=kubernetes_ip,
            kubernetes_is_in_host_network=kubernetes_is_in_host_network,
            kubernetes_labels=kubernetes_labels,
            kubernetes_namespace=kubernetes_namespace,
            kubernetes_ports=kubernetes_ports,
            kubernetes_public_ip=kubernetes_public_ip,
            kubernetes_state=kubernetes_state,
            kubernetes_type=kubernetes_type,
            local_cidr=local_cidr,
            local_networks=local_networks,
            memory_max=memory_max,
            memory_usage=memory_usage,
            node_id=node_id,
            node_name=node_name,
            node_type=node_type,
            open_files=open_files,
            open_files_count=open_files_count,
            os=os,
            pid=pid,
            pod_id=pod_id,
            pod_name=pod_name,
            ppid=ppid,
            private_ip=private_ip,
            pseudo=pseudo,
            public_ip=public_ip,
            resource_group=resource_group,
            tags=tags,
            threads=threads,
            timestamp=timestamp,
            uptime=uptime,
            user_defined_tags=user_defined_tags,
            version=version,
        )

        report_metadata.additional_properties = d
        return report_metadata

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
