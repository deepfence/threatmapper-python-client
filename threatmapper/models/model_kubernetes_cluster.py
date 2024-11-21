from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_host import ModelHost


T = TypeVar("T", bound="ModelKubernetesCluster")


@_attrs_define
class ModelKubernetesCluster:
    """
    Example:
        {'hosts': [{'vulnerabilities_count': 1, 'public_ip': ['', ''], 'secrets_count': 7, 'cloud_region':
            'cloud_region', 'container_images': [{'is_deepfence_system': True, 'metadata': {'key': ''},
            'secret_scan_status': 'secret_scan_status', 'vulnerabilities_count': 4, 'secrets_count': 1,
            'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 7, 'node_name': 'node_name',
            'secret_latest_scan_id': 'secret_latest_scan_id', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'docker_image_created_at': 'docker_image_created_at', 'docker_image_tag':
            'docker_image_tag', 'malware_scan_status': 'malware_scan_status', 'docker_image_size': 'docker_image_size',
            'image_node_id': 'image_node_id', 'docker_image_virtual_size': 'docker_image_virtual_size', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'docker_image_id': 'docker_image_id', 'vulnerability_scan_status': 'vulnerability_scan_status',
            'docker_image_name': 'docker_image_name', 'docker_image_tag_list': ['docker_image_tag_list',
            'docker_image_tag_list'], 'node_id': 'node_id'}, {'is_deepfence_system': True, 'metadata': {'key': ''},
            'secret_scan_status': 'secret_scan_status', 'vulnerabilities_count': 4, 'secrets_count': 1,
            'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 7, 'node_name': 'node_name',
            'secret_latest_scan_id': 'secret_latest_scan_id', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'docker_image_created_at': 'docker_image_created_at', 'docker_image_tag':
            'docker_image_tag', 'malware_scan_status': 'malware_scan_status', 'docker_image_size': 'docker_image_size',
            'image_node_id': 'image_node_id', 'docker_image_virtual_size': 'docker_image_virtual_size', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'docker_image_id': 'docker_image_id', 'vulnerability_scan_status': 'vulnerability_scan_status',
            'docker_image_name': 'docker_image_name', 'docker_image_tag_list': ['docker_image_tag_list',
            'docker_image_tag_list'], 'node_id': 'node_id'}], 'cpu_max': 1.4658129805029452, 'memory_usage': 4,
            'private_ip': ['', ''], 'secret_latest_scan_id': 'secret_latest_scan_id', 'exploitable_vulnerabilities_count':
            7, 'cloud_account_id': 'cloud_account_id', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'resource_group': 'resource_group', 'malware_scan_status': 'malware_scan_status', 'exploitable_malwares_count':
            5, 'inbound_connections': [{'count': 9, 'node_name': 'node_name', 'ips': ['', ''], 'node_id': 'node_id'},
            {'count': 9, 'node_name': 'node_name', 'ips': ['', ''], 'node_id': 'node_id'}], 'availability_zone':
            'availability_zone', 'is_console_vm': True, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9,
            'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109,
            'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status', 'compliance_scan_status':
            'compliance_scan_status', 'outbound_connections': [{'count': 9, 'node_name': 'node_name', 'ips': ['', ''],
            'node_id': 'node_id'}, {'count': 9, 'node_name': 'node_name', 'ips': ['', ''], 'node_id': 'node_id'}], 'os':
            'os', 'local_cidr': ['', ''], 'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 3,
            'node_name': 'node_name', 'cloud_provider': 'cloud_provider', 'agent_running': True, 'cloud_warn_alarm_count':
            0, 'exploitable_secrets_count': 2, 'version': 'version', 'uptime': 1, 'memory_max': 2, 'instance_id':
            'instance_id', 'kernel_id': 'kernel_id', 'compliances_count': 6, 'kernel_version': 'kernel_version',
            'compliance_latest_scan_id': 'compliance_latest_scan_id', 'warn_alarm_count': 1, 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'pods': [{'is_deepfence_system': True, 'kubernetes_ip': 'kubernetes_ip', 'processes': [{'memory_max': 9,
            'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109,
            'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status':
            'secret_scan_status', 'kubernetes_cluster_id': 'kubernetes_cluster_id', 'kubernetes_cluster_name':
            'kubernetes_cluster_name', 'kubernetes_state': 'kubernetes_state', 'node_name': 'node_name',
            'kubernetes_created': 'kubernetes_created', 'pod_name': 'pod_name', 'kubernetes_namespace':
            'kubernetes_namespace', 'kubernetes_is_in_host_network': True, 'malware_scan_status': 'malware_scan_status',
            'kubernetes_labels': {'key': ''}, 'containers': [{'vulnerabilities_count': 6, 'secrets_count': 1,
            'kubernetes_cluster_name': 'kubernetes_cluster_name', 'docker_container_state': 'docker_container_state',
            'cpu_max': 0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status':
            'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system':
            True, 'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline':
            'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2,
            'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id',
            'ppid': 7}], 'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'is_deepfence_system': True, 'kubernetes_ip': 'kubernetes_ip', 'processes': [{'memory_max': 9, 'cmdline':
            'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2,
            'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id',
            'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'kubernetes_state': 'kubernetes_state', 'node_name': 'node_name', 'kubernetes_created': 'kubernetes_created',
            'pod_name': 'pod_name', 'kubernetes_namespace': 'kubernetes_namespace', 'kubernetes_is_in_host_network': True,
            'malware_scan_status': 'malware_scan_status', 'kubernetes_labels': {'key': ''}, 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'cpu_usage': 5.962133916683182, 'instance_type': 'instance_type', 'vulnerability_scan_status':
            'vulnerability_scan_status', 'host_name': 'host_name', 'local_networks': ['', ''], 'node_id': 'node_id'},
            {'vulnerabilities_count': 1, 'public_ip': ['', ''], 'secrets_count': 7, 'cloud_region': 'cloud_region',
            'container_images': [{'is_deepfence_system': True, 'metadata': {'key': ''}, 'secret_scan_status':
            'secret_scan_status', 'vulnerabilities_count': 4, 'secrets_count': 1, 'malware_latest_scan_id':
            'malware_latest_scan_id', 'malwares_count': 7, 'node_name': 'node_name', 'secret_latest_scan_id':
            'secret_latest_scan_id', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'docker_image_created_at': 'docker_image_created_at', 'docker_image_tag': 'docker_image_tag',
            'malware_scan_status': 'malware_scan_status', 'docker_image_size': 'docker_image_size', 'image_node_id':
            'image_node_id', 'docker_image_virtual_size': 'docker_image_virtual_size', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'docker_image_id': 'docker_image_id', 'vulnerability_scan_status': 'vulnerability_scan_status',
            'docker_image_name': 'docker_image_name', 'docker_image_tag_list': ['docker_image_tag_list',
            'docker_image_tag_list'], 'node_id': 'node_id'}, {'is_deepfence_system': True, 'metadata': {'key': ''},
            'secret_scan_status': 'secret_scan_status', 'vulnerabilities_count': 4, 'secrets_count': 1,
            'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 7, 'node_name': 'node_name',
            'secret_latest_scan_id': 'secret_latest_scan_id', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'docker_image_created_at': 'docker_image_created_at', 'docker_image_tag':
            'docker_image_tag', 'malware_scan_status': 'malware_scan_status', 'docker_image_size': 'docker_image_size',
            'image_node_id': 'image_node_id', 'docker_image_virtual_size': 'docker_image_virtual_size', 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'docker_image_id': 'docker_image_id', 'vulnerability_scan_status': 'vulnerability_scan_status',
            'docker_image_name': 'docker_image_name', 'docker_image_tag_list': ['docker_image_tag_list',
            'docker_image_tag_list'], 'node_id': 'node_id'}], 'cpu_max': 1.4658129805029452, 'memory_usage': 4,
            'private_ip': ['', ''], 'secret_latest_scan_id': 'secret_latest_scan_id', 'exploitable_vulnerabilities_count':
            7, 'cloud_account_id': 'cloud_account_id', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'resource_group': 'resource_group', 'malware_scan_status': 'malware_scan_status', 'exploitable_malwares_count':
            5, 'inbound_connections': [{'count': 9, 'node_name': 'node_name', 'ips': ['', ''], 'node_id': 'node_id'},
            {'count': 9, 'node_name': 'node_name', 'ips': ['', ''], 'node_id': 'node_id'}], 'availability_zone':
            'availability_zone', 'is_console_vm': True, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9,
            'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109,
            'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status', 'compliance_scan_status':
            'compliance_scan_status', 'outbound_connections': [{'count': 9, 'node_name': 'node_name', 'ips': ['', ''],
            'node_id': 'node_id'}, {'count': 9, 'node_name': 'node_name', 'ips': ['', ''], 'node_id': 'node_id'}], 'os':
            'os', 'local_cidr': ['', ''], 'malware_latest_scan_id': 'malware_latest_scan_id', 'malwares_count': 3,
            'node_name': 'node_name', 'cloud_provider': 'cloud_provider', 'agent_running': True, 'cloud_warn_alarm_count':
            0, 'exploitable_secrets_count': 2, 'version': 'version', 'uptime': 1, 'memory_max': 2, 'instance_id':
            'instance_id', 'kernel_id': 'kernel_id', 'compliances_count': 6, 'kernel_version': 'kernel_version',
            'compliance_latest_scan_id': 'compliance_latest_scan_id', 'warn_alarm_count': 1, 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'pods': [{'is_deepfence_system': True, 'kubernetes_ip': 'kubernetes_ip', 'processes': [{'memory_max': 9,
            'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3,
            'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109,
            'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status':
            'secret_scan_status', 'kubernetes_cluster_id': 'kubernetes_cluster_id', 'kubernetes_cluster_name':
            'kubernetes_cluster_name', 'kubernetes_state': 'kubernetes_state', 'node_name': 'node_name',
            'kubernetes_created': 'kubernetes_created', 'pod_name': 'pod_name', 'kubernetes_namespace':
            'kubernetes_namespace', 'kubernetes_is_in_host_network': True, 'malware_scan_status': 'malware_scan_status',
            'kubernetes_labels': {'key': ''}, 'containers': [{'vulnerabilities_count': 6, 'secrets_count': 1,
            'kubernetes_cluster_name': 'kubernetes_cluster_name', 'docker_container_state': 'docker_container_state',
            'cpu_max': 0.8008281904610115, 'memory_usage': 5, 'secret_latest_scan_id': 'secret_latest_scan_id',
            'docker_container_network_mode': 'docker_container_network_mode', 'vulnerability_latest_scan_id':
            'vulnerability_latest_scan_id', 'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status':
            'malware_scan_status', 'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system':
            True, 'image': None, 'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655,
            'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name':
            'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline':
            'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2,
            'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id',
            'ppid': 7}], 'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'is_deepfence_system': True, 'kubernetes_ip': 'kubernetes_ip', 'processes': [{'memory_max': 9, 'cmdline':
            'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2,
            'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id',
            'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}], 'secret_scan_status': 'secret_scan_status',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'kubernetes_state': 'kubernetes_state', 'node_name': 'node_name', 'kubernetes_created': 'kubernetes_created',
            'pod_name': 'pod_name', 'kubernetes_namespace': 'kubernetes_namespace', 'kubernetes_is_in_host_network': True,
            'malware_scan_status': 'malware_scan_status', 'kubernetes_labels': {'key': ''}, 'containers':
            [{'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'},
            {'vulnerabilities_count': 6, 'secrets_count': 1, 'kubernetes_cluster_name': 'kubernetes_cluster_name',
            'docker_container_state': 'docker_container_state', 'cpu_max': 0.8008281904610115, 'memory_usage': 5,
            'secret_latest_scan_id': 'secret_latest_scan_id', 'docker_container_network_mode':
            'docker_container_network_mode', 'vulnerability_latest_scan_id': 'vulnerability_latest_scan_id',
            'kubernetes_namespace': 'kubernetes_namespace', 'malware_scan_status': 'malware_scan_status',
            'docker_container_ips': ['', ''], 'docker_labels': {'key': ''}, 'is_deepfence_system': True, 'image': None,
            'processes': [{'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name',
            'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'short_name': 'short_name', 'cpu_usage':
            7.061401241503109, 'node_id': 'node_id', 'ppid': 7}, {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max':
            2.3021358869347655, 'node_name': 'node_name', 'memory_usage': 3, 'open_files_count': 2, 'threads': 1, 'pid': 4,
            'short_name': 'short_name', 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid': 7}],
            'secret_scan_status': 'secret_scan_status', 'docker_container_name': 'docker_container_name',
            'docker_container_created': 'docker_container_created', 'malware_latest_scan_id': 'malware_latest_scan_id',
            'kubernetes_cluster_id': 'kubernetes_cluster_id', 'malwares_count': 1, 'node_name': 'node_name',
            'docker_container_networks': 'docker_container_networks', 'docker_container_command':
            'docker_container_command', 'uptime': 1, 'memory_max': 5, 'docker_container_ports': 'docker_container_ports',
            'docker_container_state_human': 'docker_container_state_human', 'cpu_usage': 6.027456183070403,
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'vulnerability_scan_status': 'vulnerability_scan_status', 'host_name': 'host_name', 'node_id': 'node_id'}],
            'cpu_usage': 5.962133916683182, 'instance_type': 'instance_type', 'vulnerability_scan_status':
            'vulnerability_scan_status', 'host_name': 'host_name', 'local_networks': ['', ''], 'node_id': 'node_id'}],
            'node_name': 'node_name', 'agent_running': True, 'node_id': 'node_id'}

    Attributes:
        agent_running (bool):
        hosts (Union[List['ModelHost'], None]):
        node_id (str):
        node_name (str):
    """

    agent_running: bool
    hosts: Union[List["ModelHost"], None]
    node_id: str
    node_name: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_running = self.agent_running

        hosts: Union[List[Dict[str, Any]], None]
        if isinstance(self.hosts, list):
            hosts = []
            for hosts_type_0_item_data in self.hosts:
                hosts_type_0_item = hosts_type_0_item_data.to_dict()
                hosts.append(hosts_type_0_item)

        else:
            hosts = self.hosts

        node_id = self.node_id

        node_name = self.node_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent_running": agent_running,
                "hosts": hosts,
                "node_id": node_id,
                "node_name": node_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_host import ModelHost

        d = src_dict.copy()
        agent_running = d.pop("agent_running")

        def _parse_hosts(data: object) -> Union[List["ModelHost"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hosts_type_0 = []
                _hosts_type_0 = data
                for hosts_type_0_item_data in _hosts_type_0:
                    hosts_type_0_item = ModelHost.from_dict(hosts_type_0_item_data)

                    hosts_type_0.append(hosts_type_0_item)

                return hosts_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelHost"], None], data)

        hosts = _parse_hosts(d.pop("hosts"))

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        model_kubernetes_cluster = cls(
            agent_running=agent_running,
            hosts=hosts,
            node_id=node_id,
            node_name=node_name,
        )

        model_kubernetes_cluster.additional_properties = d
        return model_kubernetes_cluster

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
