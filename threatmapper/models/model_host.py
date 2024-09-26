from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_connection import ModelConnection
    from ..models.model_container import ModelContainer
    from ..models.model_container_image import ModelContainerImage
    from ..models.model_pod import ModelPod
    from ..models.model_process import ModelProcess


T = TypeVar("T", bound="ModelHost")


@_attrs_define
class ModelHost:
    """
    Attributes:
        agent_running (bool):
        availability_zone (str):
        cloud_account_id (str):
        cloud_provider (str):
        cloud_region (str):
        cloud_warn_alarm_count (int):
        compliance_latest_scan_id (str):
        compliance_scan_status (str):
        compliances_count (int):
        container_images (Union[List['ModelContainerImage'], None]):
        containers (Union[List['ModelContainer'], None]):
        cpu_max (float):
        cpu_usage (float):
        exploitable_malwares_count (int):
        exploitable_secrets_count (int):
        exploitable_vulnerabilities_count (int):
        host_name (str):
        inbound_connections (Union[List['ModelConnection'], None]):
        instance_id (str):
        instance_type (str):
        is_console_vm (bool):
        kernel_id (str):
        kernel_version (str):
        local_cidr (Union[List[Any], None]):
        local_networks (Union[List[Any], None]):
        malware_latest_scan_id (str):
        malware_scan_status (str):
        malwares_count (int):
        memory_max (int):
        memory_usage (int):
        node_id (str):
        node_name (str):
        os (str):
        outbound_connections (Union[List['ModelConnection'], None]):
        pods (Union[List['ModelPod'], None]):
        private_ip (Union[List[Any], None]):
        processes (Union[List['ModelProcess'], None]):
        public_ip (Union[List[Any], None]):
        resource_group (str):
        secret_latest_scan_id (str):
        secret_scan_status (str):
        secrets_count (int):
        uptime (int):
        version (str):
        vulnerabilities_count (int):
        vulnerability_latest_scan_id (str):
        vulnerability_scan_status (str):
        warn_alarm_count (int):
    """

    agent_running: bool
    availability_zone: str
    cloud_account_id: str
    cloud_provider: str
    cloud_region: str
    cloud_warn_alarm_count: int
    compliance_latest_scan_id: str
    compliance_scan_status: str
    compliances_count: int
    container_images: Union[List["ModelContainerImage"], None]
    containers: Union[List["ModelContainer"], None]
    cpu_max: float
    cpu_usage: float
    exploitable_malwares_count: int
    exploitable_secrets_count: int
    exploitable_vulnerabilities_count: int
    host_name: str
    inbound_connections: Union[List["ModelConnection"], None]
    instance_id: str
    instance_type: str
    is_console_vm: bool
    kernel_id: str
    kernel_version: str
    local_cidr: Union[List[Any], None]
    local_networks: Union[List[Any], None]
    malware_latest_scan_id: str
    malware_scan_status: str
    malwares_count: int
    memory_max: int
    memory_usage: int
    node_id: str
    node_name: str
    os: str
    outbound_connections: Union[List["ModelConnection"], None]
    pods: Union[List["ModelPod"], None]
    private_ip: Union[List[Any], None]
    processes: Union[List["ModelProcess"], None]
    public_ip: Union[List[Any], None]
    resource_group: str
    secret_latest_scan_id: str
    secret_scan_status: str
    secrets_count: int
    uptime: int
    version: str
    vulnerabilities_count: int
    vulnerability_latest_scan_id: str
    vulnerability_scan_status: str
    warn_alarm_count: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_running = self.agent_running

        availability_zone = self.availability_zone

        cloud_account_id = self.cloud_account_id

        cloud_provider = self.cloud_provider

        cloud_region = self.cloud_region

        cloud_warn_alarm_count = self.cloud_warn_alarm_count

        compliance_latest_scan_id = self.compliance_latest_scan_id

        compliance_scan_status = self.compliance_scan_status

        compliances_count = self.compliances_count

        container_images: Union[List[Dict[str, Any]], None]
        if isinstance(self.container_images, list):
            container_images = []
            for container_images_type_0_item_data in self.container_images:
                container_images_type_0_item = container_images_type_0_item_data.to_dict()
                container_images.append(container_images_type_0_item)

        else:
            container_images = self.container_images

        containers: Union[List[Dict[str, Any]], None]
        if isinstance(self.containers, list):
            containers = []
            for containers_type_0_item_data in self.containers:
                containers_type_0_item = containers_type_0_item_data.to_dict()
                containers.append(containers_type_0_item)

        else:
            containers = self.containers

        cpu_max = self.cpu_max

        cpu_usage = self.cpu_usage

        exploitable_malwares_count = self.exploitable_malwares_count

        exploitable_secrets_count = self.exploitable_secrets_count

        exploitable_vulnerabilities_count = self.exploitable_vulnerabilities_count

        host_name = self.host_name

        inbound_connections: Union[List[Dict[str, Any]], None]
        if isinstance(self.inbound_connections, list):
            inbound_connections = []
            for inbound_connections_type_0_item_data in self.inbound_connections:
                inbound_connections_type_0_item = inbound_connections_type_0_item_data.to_dict()
                inbound_connections.append(inbound_connections_type_0_item)

        else:
            inbound_connections = self.inbound_connections

        instance_id = self.instance_id

        instance_type = self.instance_type

        is_console_vm = self.is_console_vm

        kernel_id = self.kernel_id

        kernel_version = self.kernel_version

        local_cidr: Union[List[Any], None]
        if isinstance(self.local_cidr, list):
            local_cidr = self.local_cidr

        else:
            local_cidr = self.local_cidr

        local_networks: Union[List[Any], None]
        if isinstance(self.local_networks, list):
            local_networks = self.local_networks

        else:
            local_networks = self.local_networks

        malware_latest_scan_id = self.malware_latest_scan_id

        malware_scan_status = self.malware_scan_status

        malwares_count = self.malwares_count

        memory_max = self.memory_max

        memory_usage = self.memory_usage

        node_id = self.node_id

        node_name = self.node_name

        os = self.os

        outbound_connections: Union[List[Dict[str, Any]], None]
        if isinstance(self.outbound_connections, list):
            outbound_connections = []
            for outbound_connections_type_0_item_data in self.outbound_connections:
                outbound_connections_type_0_item = outbound_connections_type_0_item_data.to_dict()
                outbound_connections.append(outbound_connections_type_0_item)

        else:
            outbound_connections = self.outbound_connections

        pods: Union[List[Dict[str, Any]], None]
        if isinstance(self.pods, list):
            pods = []
            for pods_type_0_item_data in self.pods:
                pods_type_0_item = pods_type_0_item_data.to_dict()
                pods.append(pods_type_0_item)

        else:
            pods = self.pods

        private_ip: Union[List[Any], None]
        if isinstance(self.private_ip, list):
            private_ip = self.private_ip

        else:
            private_ip = self.private_ip

        processes: Union[List[Dict[str, Any]], None]
        if isinstance(self.processes, list):
            processes = []
            for processes_type_0_item_data in self.processes:
                processes_type_0_item = processes_type_0_item_data.to_dict()
                processes.append(processes_type_0_item)

        else:
            processes = self.processes

        public_ip: Union[List[Any], None]
        if isinstance(self.public_ip, list):
            public_ip = self.public_ip

        else:
            public_ip = self.public_ip

        resource_group = self.resource_group

        secret_latest_scan_id = self.secret_latest_scan_id

        secret_scan_status = self.secret_scan_status

        secrets_count = self.secrets_count

        uptime = self.uptime

        version = self.version

        vulnerabilities_count = self.vulnerabilities_count

        vulnerability_latest_scan_id = self.vulnerability_latest_scan_id

        vulnerability_scan_status = self.vulnerability_scan_status

        warn_alarm_count = self.warn_alarm_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_running": agent_running,
                "availability_zone": availability_zone,
                "cloud_account_id": cloud_account_id,
                "cloud_provider": cloud_provider,
                "cloud_region": cloud_region,
                "cloud_warn_alarm_count": cloud_warn_alarm_count,
                "compliance_latest_scan_id": compliance_latest_scan_id,
                "compliance_scan_status": compliance_scan_status,
                "compliances_count": compliances_count,
                "container_images": container_images,
                "containers": containers,
                "cpu_max": cpu_max,
                "cpu_usage": cpu_usage,
                "exploitable_malwares_count": exploitable_malwares_count,
                "exploitable_secrets_count": exploitable_secrets_count,
                "exploitable_vulnerabilities_count": exploitable_vulnerabilities_count,
                "host_name": host_name,
                "inbound_connections": inbound_connections,
                "instance_id": instance_id,
                "instance_type": instance_type,
                "is_console_vm": is_console_vm,
                "kernel_id": kernel_id,
                "kernel_version": kernel_version,
                "local_cidr": local_cidr,
                "local_networks": local_networks,
                "malware_latest_scan_id": malware_latest_scan_id,
                "malware_scan_status": malware_scan_status,
                "malwares_count": malwares_count,
                "memory_max": memory_max,
                "memory_usage": memory_usage,
                "node_id": node_id,
                "node_name": node_name,
                "os": os,
                "outbound_connections": outbound_connections,
                "pods": pods,
                "private_ip": private_ip,
                "processes": processes,
                "public_ip": public_ip,
                "resource_group": resource_group,
                "secret_latest_scan_id": secret_latest_scan_id,
                "secret_scan_status": secret_scan_status,
                "secrets_count": secrets_count,
                "uptime": uptime,
                "version": version,
                "vulnerabilities_count": vulnerabilities_count,
                "vulnerability_latest_scan_id": vulnerability_latest_scan_id,
                "vulnerability_scan_status": vulnerability_scan_status,
                "warn_alarm_count": warn_alarm_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_connection import ModelConnection
        from ..models.model_container import ModelContainer
        from ..models.model_container_image import ModelContainerImage
        from ..models.model_pod import ModelPod
        from ..models.model_process import ModelProcess

        d = src_dict.copy()
        agent_running = d.pop("agent_running")

        availability_zone = d.pop("availability_zone")

        cloud_account_id = d.pop("cloud_account_id")

        cloud_provider = d.pop("cloud_provider")

        cloud_region = d.pop("cloud_region")

        cloud_warn_alarm_count = d.pop("cloud_warn_alarm_count")

        compliance_latest_scan_id = d.pop("compliance_latest_scan_id")

        compliance_scan_status = d.pop("compliance_scan_status")

        compliances_count = d.pop("compliances_count")

        def _parse_container_images(data: object) -> Union[List["ModelContainerImage"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                container_images_type_0 = []
                _container_images_type_0 = data
                for container_images_type_0_item_data in _container_images_type_0:
                    container_images_type_0_item = ModelContainerImage.from_dict(container_images_type_0_item_data)

                    container_images_type_0.append(container_images_type_0_item)

                return container_images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelContainerImage"], None], data)

        container_images = _parse_container_images(d.pop("container_images"))

        def _parse_containers(data: object) -> Union[List["ModelContainer"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                containers_type_0 = []
                _containers_type_0 = data
                for containers_type_0_item_data in _containers_type_0:
                    containers_type_0_item = ModelContainer.from_dict(containers_type_0_item_data)

                    containers_type_0.append(containers_type_0_item)

                return containers_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelContainer"], None], data)

        containers = _parse_containers(d.pop("containers"))

        cpu_max = d.pop("cpu_max")

        cpu_usage = d.pop("cpu_usage")

        exploitable_malwares_count = d.pop("exploitable_malwares_count")

        exploitable_secrets_count = d.pop("exploitable_secrets_count")

        exploitable_vulnerabilities_count = d.pop("exploitable_vulnerabilities_count")

        host_name = d.pop("host_name")

        def _parse_inbound_connections(data: object) -> Union[List["ModelConnection"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inbound_connections_type_0 = []
                _inbound_connections_type_0 = data
                for inbound_connections_type_0_item_data in _inbound_connections_type_0:
                    inbound_connections_type_0_item = ModelConnection.from_dict(inbound_connections_type_0_item_data)

                    inbound_connections_type_0.append(inbound_connections_type_0_item)

                return inbound_connections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelConnection"], None], data)

        inbound_connections = _parse_inbound_connections(d.pop("inbound_connections"))

        instance_id = d.pop("instance_id")

        instance_type = d.pop("instance_type")

        is_console_vm = d.pop("is_console_vm")

        kernel_id = d.pop("kernel_id")

        kernel_version = d.pop("kernel_version")

        def _parse_local_cidr(data: object) -> Union[List[Any], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                local_cidr_type_0 = cast(List[Any], data)

                return local_cidr_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None], data)

        local_cidr = _parse_local_cidr(d.pop("local_cidr"))

        def _parse_local_networks(data: object) -> Union[List[Any], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                local_networks_type_0 = cast(List[Any], data)

                return local_networks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None], data)

        local_networks = _parse_local_networks(d.pop("local_networks"))

        malware_latest_scan_id = d.pop("malware_latest_scan_id")

        malware_scan_status = d.pop("malware_scan_status")

        malwares_count = d.pop("malwares_count")

        memory_max = d.pop("memory_max")

        memory_usage = d.pop("memory_usage")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        os = d.pop("os")

        def _parse_outbound_connections(data: object) -> Union[List["ModelConnection"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                outbound_connections_type_0 = []
                _outbound_connections_type_0 = data
                for outbound_connections_type_0_item_data in _outbound_connections_type_0:
                    outbound_connections_type_0_item = ModelConnection.from_dict(outbound_connections_type_0_item_data)

                    outbound_connections_type_0.append(outbound_connections_type_0_item)

                return outbound_connections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelConnection"], None], data)

        outbound_connections = _parse_outbound_connections(d.pop("outbound_connections"))

        def _parse_pods(data: object) -> Union[List["ModelPod"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                pods_type_0 = []
                _pods_type_0 = data
                for pods_type_0_item_data in _pods_type_0:
                    pods_type_0_item = ModelPod.from_dict(pods_type_0_item_data)

                    pods_type_0.append(pods_type_0_item)

                return pods_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelPod"], None], data)

        pods = _parse_pods(d.pop("pods"))

        def _parse_private_ip(data: object) -> Union[List[Any], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                private_ip_type_0 = cast(List[Any], data)

                return private_ip_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None], data)

        private_ip = _parse_private_ip(d.pop("private_ip"))

        def _parse_processes(data: object) -> Union[List["ModelProcess"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                processes_type_0 = []
                _processes_type_0 = data
                for processes_type_0_item_data in _processes_type_0:
                    processes_type_0_item = ModelProcess.from_dict(processes_type_0_item_data)

                    processes_type_0.append(processes_type_0_item)

                return processes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelProcess"], None], data)

        processes = _parse_processes(d.pop("processes"))

        def _parse_public_ip(data: object) -> Union[List[Any], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                public_ip_type_0 = cast(List[Any], data)

                return public_ip_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None], data)

        public_ip = _parse_public_ip(d.pop("public_ip"))

        resource_group = d.pop("resource_group")

        secret_latest_scan_id = d.pop("secret_latest_scan_id")

        secret_scan_status = d.pop("secret_scan_status")

        secrets_count = d.pop("secrets_count")

        uptime = d.pop("uptime")

        version = d.pop("version")

        vulnerabilities_count = d.pop("vulnerabilities_count")

        vulnerability_latest_scan_id = d.pop("vulnerability_latest_scan_id")

        vulnerability_scan_status = d.pop("vulnerability_scan_status")

        warn_alarm_count = d.pop("warn_alarm_count")

        model_host = cls(
            agent_running=agent_running,
            availability_zone=availability_zone,
            cloud_account_id=cloud_account_id,
            cloud_provider=cloud_provider,
            cloud_region=cloud_region,
            cloud_warn_alarm_count=cloud_warn_alarm_count,
            compliance_latest_scan_id=compliance_latest_scan_id,
            compliance_scan_status=compliance_scan_status,
            compliances_count=compliances_count,
            container_images=container_images,
            containers=containers,
            cpu_max=cpu_max,
            cpu_usage=cpu_usage,
            exploitable_malwares_count=exploitable_malwares_count,
            exploitable_secrets_count=exploitable_secrets_count,
            exploitable_vulnerabilities_count=exploitable_vulnerabilities_count,
            host_name=host_name,
            inbound_connections=inbound_connections,
            instance_id=instance_id,
            instance_type=instance_type,
            is_console_vm=is_console_vm,
            kernel_id=kernel_id,
            kernel_version=kernel_version,
            local_cidr=local_cidr,
            local_networks=local_networks,
            malware_latest_scan_id=malware_latest_scan_id,
            malware_scan_status=malware_scan_status,
            malwares_count=malwares_count,
            memory_max=memory_max,
            memory_usage=memory_usage,
            node_id=node_id,
            node_name=node_name,
            os=os,
            outbound_connections=outbound_connections,
            pods=pods,
            private_ip=private_ip,
            processes=processes,
            public_ip=public_ip,
            resource_group=resource_group,
            secret_latest_scan_id=secret_latest_scan_id,
            secret_scan_status=secret_scan_status,
            secrets_count=secrets_count,
            uptime=uptime,
            version=version,
            vulnerabilities_count=vulnerabilities_count,
            vulnerability_latest_scan_id=vulnerability_latest_scan_id,
            vulnerability_scan_status=vulnerability_scan_status,
            warn_alarm_count=warn_alarm_count,
        )

        model_host.additional_properties = d
        return model_host

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
