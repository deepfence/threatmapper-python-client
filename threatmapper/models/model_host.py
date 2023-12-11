from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, cast

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
    Example:
        {'vulnerabilities_count': 2, 'public_ip': ['', ''], 'secrets_count': 9, 'cloud_region': 'cloud_region',
            'container_images': [{'metadata': {'key': ''}, 'secret_scan_status': 'secret_scan_status',
            'vulnerabilities_count': 4, 'secrets_count': 1, 'malware_latest_scan_id': 'malware_latest_scan_id',
            'malwares_count': 7, 'node_name': 'node_name', 'secret_latest_scan_id': 'secret_latest_scan_id',
            'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id', 'docker_image_created_at':
            'docker_image_created_at', 'docker_image_tag': 'docker_image_tag', 'malware_scan_status': 'malware_scan_status',
            'docker_image_size': 'docker_image_size', 'image_node_id': 'image_node_id', 'docker_image_virtual_size':
            'docker_image_virtual_size', 'containers': [{'vulnerabilities_count': 6, 'secrets_count': 1,
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''},
            'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name':
            'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name',
            'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline',
            'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1,
            'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'malwares_count': 1, 'node_name': 'node_name', 'docker_container_networks': 'docker_container_networks',
            'docker_container_command': 'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports':
            'docker_container_ports', 'docker_container_state_human': 'docker_container_state_human', 'cpu_usage':
            6.027456183070403, 'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name',
            'node_id': 'node_id'}, {'vulnerabilities_count': 6, 'secrets_count': 1, 'docker_container_state':
            'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id':
            'secret_latest_scan_id', 'docker_container_network_mode': 'docker_container_network_mode',
            'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'image': None, 'processes': [{'memory_max': 9,
            'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109,
            'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status':
            'secret_scan_status', 'docker_container_name': 'docker_container_name', 'docker_container_created':
            'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 1,
            'node_name': 'node_name', 'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'docker_image_id': 'docker_image_id', 'vulnerability_scan_status': 'vulnerability_scan_status',
            'docker_image_name': 'docker_image_name', 'docker_image_tag_list': ['docker_image_tag_list',
            'docker_image_tag_list'], 'node_id': 'node_id'}, {'metadata': {'key': ''}, 'secret_scan_status':
            'secret_scan_status', 'vulnerabilities_count': 4, 'secrets_count': 1, 'malware_latest_scan_id':
            'malware_latest_scan_id', 'malwares_count': 7, 'node_name': 'node_name', 'secret_latest_scan_id':
            'secret_latest_scan_id', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'docker_image_created_at': 'docker_image_created_at', 'docker_image_tag': 'docker_image_tag',
            'malware_scan_status': 'malware_scan_status', 'docker_image_size': 'docker_image_size', 'image_node_id':
            'image_node_id', 'docker_image_virtual_size': 'docker_image_virtual_size', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'docker_container_state': 'docker_container_state', 'cpu_max':
            0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''],
            'docker_labels': {'key': ''}, 'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9,
            'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109,
            'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status', 'docker_container_name':
            'docker_container_name', 'docker_container_created': 'docker_container_created', 'malware_latest_scan_id':
            'malware_latest_scan_id', 'malwares_count': 1, 'node_name': 'node_name', 'docker_container_networks':
            'docker_container_networks', 'docker_container_command': 'docker_container_command', 'uptime': 1, 'memory_max':
            5, 'docker_container_ports': 'docker_container_ports', 'docker_container_state_human':
            'docker_container_state_human', 'cpu_usage': 6.027456183070403, 'vulnerability_scan_status':
            'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}, {'vulnerabilities_count': 6,
            'secrets_count': 1, 'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115,
            'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''},
            'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name':
            'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name',
            'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline',
            'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1,
            'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'malwares_count': 1, 'node_name': 'node_name', 'docker_container_networks': 'docker_container_networks',
            'docker_container_command': 'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports':
            'docker_container_ports', 'docker_container_state_human': 'docker_container_state_human', 'cpu_usage':
            6.027456183070403, 'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name',
            'node_id': 'node_id'}], 'docker_image_id': 'docker_image_id', 'vulnerability_scan_status':
            'vulnerability_scan_status', 'docker_image_name': 'docker_image_name', 'docker_image_tag_list':
            ['docker_image_tag_list', 'docker_image_tag_list'], 'node_id': 'node_id'}], 'cpu_max': 6.027456183070403,
            'memory_usage': 7, 'private_ip': ['', ''], 'secret_latest_scan_id': 'secret_latest_scan_id', 'cloud_account_id':
            'cloud_account_id', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id', 'resource_group':
            'resource_group', 'malware_scan_status': 'malware_scan_status', 'inbound_connections': [{'count': 5,
            'node_name': 'node_name', 'node_id': 'node_id'}, {'count': 5, 'node_name': 'node_name', 'node_id': 'node_id'}],
            'availability_zone': 'availability_zone', 'is_console_vm': True, 'processes': [{'memory_max': 9, 'cmdline':
            'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2,
            'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id',
            'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status',
            'compliance_scan_status': 'compliance_scan_status', 'outbound_connections': [{'count': 5, 'node_name':
            'node_name', 'node_id': 'node_id'}, {'count': 5, 'node_name': 'node_name', 'node_id': 'node_id'}], 'os': 'os',
            'local_cidr': ['', ''], 'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 5, 'node_name':
            'node_name', 'cloud_provider': 'cloud_provider', 'agent_running': True, 'version': 'version', 'uptime': 3,
            'memory_max': 2, 'instance_id': 'instance_id', 'kernel_id': 'kernel_id', 'compliances_count': 0,
            'kernel_version': 'kernel_version', 'compliance_latest_scan_id': 'compliance_latest_scan_id', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'docker_container_state': 'docker_container_state', 'cpu_max':
            0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''],
            'docker_labels': {'key': ''}, 'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9,
            'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109,
            'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status', 'docker_container_name':
            'docker_container_name', 'docker_container_created': 'docker_container_created', 'malware_latest_scan_id':
            'malware_latest_scan_id', 'malwares_count': 1, 'node_name': 'node_name', 'docker_container_networks':
            'docker_container_networks', 'docker_container_command': 'docker_container_command', 'uptime': 1, 'memory_max':
            5, 'docker_container_ports': 'docker_container_ports', 'docker_container_state_human':
            'docker_container_state_human', 'cpu_usage': 6.027456183070403, 'vulnerability_scan_status':
            'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}, {'vulnerabilities_count': 6,
            'secrets_count': 1, 'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115,
            'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''},
            'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name':
            'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name',
            'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline',
            'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1,
            'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'malwares_count': 1, 'node_name': 'node_name', 'docker_container_networks': 'docker_container_networks',
            'docker_container_command': 'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports':
            'docker_container_ports', 'docker_container_state_human': 'docker_container_state_human', 'cpu_usage':
            6.027456183070403, 'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name',
            'node_id': 'node_id'}], 'pods': [{'kubernetes_ip': 'kubernetes_ip', 'processes': [{'memory_max': 9, 'cmdline':
            'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2,
            'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id',
            'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'kubernetes_state': 'kubernetes_state', 'node_name': 'node_name', 'kubernetes_created': 'kubernetes_created',
            'pod_name': 'pod_name', 'kubernetes_namespace': 'kubernetes_namespace', 'kubernetes_is_in_host_network': True,
            'malware_scan_status': 'malware_scan_status', 'kubernetes_labels': {'key': ''}, 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'docker_container_state': 'docker_container_state', 'cpu_max':
            0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''],
            'docker_labels': {'key': ''}, 'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9,
            'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109,
            'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status', 'docker_container_name':
            'docker_container_name', 'docker_container_created': 'docker_container_created', 'malware_latest_scan_id':
            'malware_latest_scan_id', 'malwares_count': 1, 'node_name': 'node_name', 'docker_container_networks':
            'docker_container_networks', 'docker_container_command': 'docker_container_command', 'uptime': 1, 'memory_max':
            5, 'docker_container_ports': 'docker_container_ports', 'docker_container_state_human':
            'docker_container_state_human', 'cpu_usage': 6.027456183070403, 'vulnerability_scan_status':
            'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}, {'vulnerabilities_count': 6,
            'secrets_count': 1, 'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115,
            'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''},
            'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name':
            'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name',
            'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline',
            'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1,
            'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'malwares_count': 1, 'node_name': 'node_name', 'docker_container_networks': 'docker_container_networks',
            'docker_container_command': 'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports':
            'docker_container_ports', 'docker_container_state_human': 'docker_container_state_human', 'cpu_usage':
            6.027456183070403, 'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name',
            'node_id': 'node_id'}], 'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name',
            'node_id': 'node_id'}, {'kubernetes_ip': 'kubernetes_ip', 'processes': [{'memory_max': 9, 'cmdline': 'cmdline',
            'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1,
            'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7},
            {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage':
            3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109,
            'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status', 'kubernetes_cluster_id':
            'kubernetes_cluster_id', 'kubernetes_cluster_name': 'kubernetes_cluster_name', 'kubernetes_state':
            'kubernetes_state', 'node_name': 'node_name', 'kubernetes_created': 'kubernetes_created', 'pod_name':
            'pod_name', 'kubernetes_namespace': 'kubernetes_namespace', 'kubernetes_is_in_host_network': True,
            'malware_scan_status': 'malware_scan_status', 'kubernetes_labels': {'key': ''}, 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'docker_container_state': 'docker_container_state', 'cpu_max':
            0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''],
            'docker_labels': {'key': ''}, 'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9,
            'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109,
            'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status', 'docker_container_name':
            'docker_container_name', 'docker_container_created': 'docker_container_created', 'malware_latest_scan_id':
            'malware_latest_scan_id', 'malwares_count': 1, 'node_name': 'node_name', 'docker_container_networks':
            'docker_container_networks', 'docker_container_command': 'docker_container_command', 'uptime': 1, 'memory_max':
            5, 'docker_container_ports': 'docker_container_ports', 'docker_container_state_human':
            'docker_container_state_human', 'cpu_usage': 6.027456183070403, 'vulnerability_scan_status':
            'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}, {'vulnerabilities_count': 6,
            'secrets_count': 1, 'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115,
            'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'malware_scan_status': 'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''},
            'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name':
            'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name',
            'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline',
            'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1,
            'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'malwares_count': 1, 'node_name': 'node_name', 'docker_container_networks': 'docker_container_networks',
            'docker_container_command': 'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports':
            'docker_container_ports', 'docker_container_state_human': 'docker_container_state_human', 'cpu_usage':
            6.027456183070403, 'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name',
            'node_id': 'node_id'}], 'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name',
            'node_id': 'node_id'}], 'cpu_usage': 1.4658129805029452, 'instance_type': 'instance_type',
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'local_networks': ['', ''],
            'node_id': 'node_id'}

    Attributes:
        agent_running (bool):
        availability_zone (str):
        cloud_account_id (str):
        cloud_provider (str):
        cloud_region (str):
        compliance_latest_scan_id (str):
        compliance_scan_status (str):
        compliances_count (int):
        cpu_max (float):
        cpu_usage (float):
        host_name (str):
        instance_id (str):
        instance_type (str):
        is_console_vm (bool):
        kernel_id (str):
        kernel_version (str):
        malware_latest_scan_id (str):
        malware_scan_status (str):
        malwares_count (int):
        memory_max (int):
        memory_usage (int):
        node_id (str):
        node_name (str):
        os (str):
        resource_group (str):
        secret_latest_scan_id (str):
        secret_scan_status (str):
        secrets_count (int):
        uptime (int):
        version (str):
        vulnerabilities_count (int):
        vulnerability_latest_scan_id (str):
        vulnerability_scan_status (str):
        container_images (Optional[List['ModelContainerImage']]):
        containers (Optional[List['ModelContainer']]):
        inbound_connections (Optional[List['ModelConnection']]):
        local_cidr (Optional[List[Any]]):
        local_networks (Optional[List[Any]]):
        outbound_connections (Optional[List['ModelConnection']]):
        pods (Optional[List['ModelPod']]):
        private_ip (Optional[List[Any]]):
        processes (Optional[List['ModelProcess']]):
        public_ip (Optional[List[Any]]):
    """

    agent_running: bool
    availability_zone: str
    cloud_account_id: str
    cloud_provider: str
    cloud_region: str
    compliance_latest_scan_id: str
    compliance_scan_status: str
    compliances_count: int
    cpu_max: float
    cpu_usage: float
    host_name: str
    instance_id: str
    instance_type: str
    is_console_vm: bool
    kernel_id: str
    kernel_version: str
    malware_latest_scan_id: str
    malware_scan_status: str
    malwares_count: int
    memory_max: int
    memory_usage: int
    node_id: str
    node_name: str
    os: str
    resource_group: str
    secret_latest_scan_id: str
    secret_scan_status: str
    secrets_count: int
    uptime: int
    version: str
    vulnerabilities_count: int
    vulnerability_latest_scan_id: str
    vulnerability_scan_status: str
    container_images: Optional[List["ModelContainerImage"]]
    containers: Optional[List["ModelContainer"]]
    inbound_connections: Optional[List["ModelConnection"]]
    local_cidr: Optional[List[Any]]
    local_networks: Optional[List[Any]]
    outbound_connections: Optional[List["ModelConnection"]]
    pods: Optional[List["ModelPod"]]
    private_ip: Optional[List[Any]]
    processes: Optional[List["ModelProcess"]]
    public_ip: Optional[List[Any]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_running = self.agent_running
        availability_zone = self.availability_zone
        cloud_account_id = self.cloud_account_id
        cloud_provider = self.cloud_provider
        cloud_region = self.cloud_region
        compliance_latest_scan_id = self.compliance_latest_scan_id
        compliance_scan_status = self.compliance_scan_status
        compliances_count = self.compliances_count
        cpu_max = self.cpu_max
        cpu_usage = self.cpu_usage
        host_name = self.host_name
        instance_id = self.instance_id
        instance_type = self.instance_type
        is_console_vm = self.is_console_vm
        kernel_id = self.kernel_id
        kernel_version = self.kernel_version
        malware_latest_scan_id = self.malware_latest_scan_id
        malware_scan_status = self.malware_scan_status
        malwares_count = self.malwares_count
        memory_max = self.memory_max
        memory_usage = self.memory_usage
        node_id = self.node_id
        node_name = self.node_name
        os = self.os
        resource_group = self.resource_group
        secret_latest_scan_id = self.secret_latest_scan_id
        secret_scan_status = self.secret_scan_status
        secrets_count = self.secrets_count
        uptime = self.uptime
        version = self.version
        vulnerabilities_count = self.vulnerabilities_count
        vulnerability_latest_scan_id = self.vulnerability_latest_scan_id
        vulnerability_scan_status = self.vulnerability_scan_status
        if self.container_images is None:
            container_images = None
        else:
            container_images = []
            for container_images_item_data in self.container_images:
                container_images_item = container_images_item_data.to_dict()

                container_images.append(container_images_item)

        if self.containers is None:
            containers = None
        else:
            containers = []
            for containers_item_data in self.containers:
                containers_item = containers_item_data.to_dict()

                containers.append(containers_item)

        if self.inbound_connections is None:
            inbound_connections = None
        else:
            inbound_connections = []
            for inbound_connections_item_data in self.inbound_connections:
                inbound_connections_item = inbound_connections_item_data.to_dict()

                inbound_connections.append(inbound_connections_item)

        if self.local_cidr is None:
            local_cidr = None
        else:
            local_cidr = self.local_cidr

        if self.local_networks is None:
            local_networks = None
        else:
            local_networks = self.local_networks

        if self.outbound_connections is None:
            outbound_connections = None
        else:
            outbound_connections = []
            for outbound_connections_item_data in self.outbound_connections:
                outbound_connections_item = outbound_connections_item_data.to_dict()

                outbound_connections.append(outbound_connections_item)

        if self.pods is None:
            pods = None
        else:
            pods = []
            for pods_item_data in self.pods:
                pods_item = pods_item_data.to_dict()

                pods.append(pods_item)

        if self.private_ip is None:
            private_ip = None
        else:
            private_ip = self.private_ip

        if self.processes is None:
            processes = None
        else:
            processes = []
            for processes_item_data in self.processes:
                processes_item = processes_item_data.to_dict()

                processes.append(processes_item)

        if self.public_ip is None:
            public_ip = None
        else:
            public_ip = self.public_ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_running": agent_running,
                "availability_zone": availability_zone,
                "cloud_account_id": cloud_account_id,
                "cloud_provider": cloud_provider,
                "cloud_region": cloud_region,
                "compliance_latest_scan_id": compliance_latest_scan_id,
                "compliance_scan_status": compliance_scan_status,
                "compliances_count": compliances_count,
                "cpu_max": cpu_max,
                "cpu_usage": cpu_usage,
                "host_name": host_name,
                "instance_id": instance_id,
                "instance_type": instance_type,
                "is_console_vm": is_console_vm,
                "kernel_id": kernel_id,
                "kernel_version": kernel_version,
                "malware_latest_scan_id": malware_latest_scan_id,
                "malware_scan_status": malware_scan_status,
                "malwares_count": malwares_count,
                "memory_max": memory_max,
                "memory_usage": memory_usage,
                "node_id": node_id,
                "node_name": node_name,
                "os": os,
                "resource_group": resource_group,
                "secret_latest_scan_id": secret_latest_scan_id,
                "secret_scan_status": secret_scan_status,
                "secrets_count": secrets_count,
                "uptime": uptime,
                "version": version,
                "vulnerabilities_count": vulnerabilities_count,
                "vulnerability_latest_scan_id": vulnerability_latest_scan_id,
                "vulnerability_scan_status": vulnerability_scan_status,
                "container_images": container_images,
                "containers": containers,
                "inbound_connections": inbound_connections,
                "local_cidr": local_cidr,
                "local_networks": local_networks,
                "outbound_connections": outbound_connections,
                "pods": pods,
                "private_ip": private_ip,
                "processes": processes,
                "public_ip": public_ip,
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

        compliance_latest_scan_id = d.pop("compliance_latest_scan_id")

        compliance_scan_status = d.pop("compliance_scan_status")

        compliances_count = d.pop("compliances_count")

        cpu_max = d.pop("cpu_max")

        cpu_usage = d.pop("cpu_usage")

        host_name = d.pop("host_name")

        instance_id = d.pop("instance_id")

        instance_type = d.pop("instance_type")

        is_console_vm = d.pop("is_console_vm")

        kernel_id = d.pop("kernel_id")

        kernel_version = d.pop("kernel_version")

        malware_latest_scan_id = d.pop("malware_latest_scan_id")

        malware_scan_status = d.pop("malware_scan_status")

        malwares_count = d.pop("malwares_count")

        memory_max = d.pop("memory_max")

        memory_usage = d.pop("memory_usage")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        os = d.pop("os")

        resource_group = d.pop("resource_group")

        secret_latest_scan_id = d.pop("secret_latest_scan_id")

        secret_scan_status = d.pop("secret_scan_status")

        secrets_count = d.pop("secrets_count")

        uptime = d.pop("uptime")

        version = d.pop("version")

        vulnerabilities_count = d.pop("vulnerabilities_count")

        vulnerability_latest_scan_id = d.pop("vulnerability_latest_scan_id")

        vulnerability_scan_status = d.pop("vulnerability_scan_status")

        container_images = []
        _container_images = d.pop("container_images")
        for container_images_item_data in _container_images or []:
            container_images_item = ModelContainerImage.from_dict(container_images_item_data)

            container_images.append(container_images_item)

        containers = []
        _containers = d.pop("containers")
        for containers_item_data in _containers or []:
            containers_item = ModelContainer.from_dict(containers_item_data)

            containers.append(containers_item)

        inbound_connections = []
        _inbound_connections = d.pop("inbound_connections")
        for inbound_connections_item_data in _inbound_connections or []:
            inbound_connections_item = ModelConnection.from_dict(inbound_connections_item_data)

            inbound_connections.append(inbound_connections_item)

        local_cidr = cast(List[Any], d.pop("local_cidr"))

        local_networks = cast(List[Any], d.pop("local_networks"))

        outbound_connections = []
        _outbound_connections = d.pop("outbound_connections")
        for outbound_connections_item_data in _outbound_connections or []:
            outbound_connections_item = ModelConnection.from_dict(outbound_connections_item_data)

            outbound_connections.append(outbound_connections_item)

        pods = []
        _pods = d.pop("pods")
        for pods_item_data in _pods or []:
            pods_item = ModelPod.from_dict(pods_item_data)

            pods.append(pods_item)

        private_ip = cast(List[Any], d.pop("private_ip"))

        processes = []
        _processes = d.pop("processes")
        for processes_item_data in _processes or []:
            processes_item = ModelProcess.from_dict(processes_item_data)

            processes.append(processes_item)

        public_ip = cast(List[Any], d.pop("public_ip"))

        model_host = cls(
            agent_running=agent_running,
            availability_zone=availability_zone,
            cloud_account_id=cloud_account_id,
            cloud_provider=cloud_provider,
            cloud_region=cloud_region,
            compliance_latest_scan_id=compliance_latest_scan_id,
            compliance_scan_status=compliance_scan_status,
            compliances_count=compliances_count,
            cpu_max=cpu_max,
            cpu_usage=cpu_usage,
            host_name=host_name,
            instance_id=instance_id,
            instance_type=instance_type,
            is_console_vm=is_console_vm,
            kernel_id=kernel_id,
            kernel_version=kernel_version,
            malware_latest_scan_id=malware_latest_scan_id,
            malware_scan_status=malware_scan_status,
            malwares_count=malwares_count,
            memory_max=memory_max,
            memory_usage=memory_usage,
            node_id=node_id,
            node_name=node_name,
            os=os,
            resource_group=resource_group,
            secret_latest_scan_id=secret_latest_scan_id,
            secret_scan_status=secret_scan_status,
            secrets_count=secrets_count,
            uptime=uptime,
            version=version,
            vulnerabilities_count=vulnerabilities_count,
            vulnerability_latest_scan_id=vulnerability_latest_scan_id,
            vulnerability_scan_status=vulnerability_scan_status,
            container_images=container_images,
            containers=containers,
            inbound_connections=inbound_connections,
            local_cidr=local_cidr,
            local_networks=local_networks,
            outbound_connections=outbound_connections,
            pods=pods,
            private_ip=private_ip,
            processes=processes,
            public_ip=public_ip,
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
