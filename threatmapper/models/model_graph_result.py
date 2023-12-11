from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_graph_result_edges import ModelGraphResultEdges
    from ..models.model_graph_result_nodes import ModelGraphResultNodes


T = TypeVar("T", bound="ModelGraphResult")


@_attrs_define
class ModelGraphResult:
    """
    Example:
        {'nodes': {'key': {'immediate_parent_id': 'immediate_parent_id', 'metadata': {'docker_image_name_with_tag':
            'docker_image_name_with_tag', 'kubernetes_ip': 'kubernetes_ip', 'public_ip': ['public_ip', 'public_ip'],
            'kubernetes_cluster_name': 'kubernetes_cluster_name', 'docker_container_state': 'docker_container_state',
            'cpu_max': 6.027456183070403, 'pid': 7, 'kubernetes_created': 'kubernetes_created', 'kubernetes_namespace':
            'kubernetes_namespace', 'cmdline': 'cmdline', 'node_type': 'node_type', 'interface_ip_map': 'interface_ip_map',
            'pseudo': True, 'docker_container_name': 'docker_container_name', 'docker_container_created':
            'docker_container_created', 'kubernetes_cluster_id': 'kubernetes_cluster_id', 'docker_container_networks':
            'docker_container_networks', 'kubernetes_ports': ['kubernetes_ports', 'kubernetes_ports'], 'version': 'version',
            'pod_name': 'pod_name', 'ppid': 9, 'tags': ['tags', 'tags'], 'docker_container_ports': 'docker_container_ports',
            'kubernetes_is_in_host_network': True, 'instance_id': 'instance_id', 'kernel_id': 'kernel_id', 'copy_of':
            'copy_of', 'open_files': ['open_files', 'open_files'], 'docker_env': 'docker_env', 'connection_count': 0,
            'docker_image_size': 'docker_image_size', 'short_name': 'short_name', 'cpu_usage': 1.4658129805029452, 'pod_id':
            'pod_id', 'docker_label': 'docker_label', 'instance_type': 'instance_type', 'docker_image_name':
            'docker_image_name', 'user_defined_tags': ['user_defined_tags', 'user_defined_tags'], 'local_networks':
            ['local_networks', 'local_networks'], 'cloud_region': 'cloud_region', 'kubernetes_state': 'kubernetes_state',
            'interface_names': ['interface_names', 'interface_names'], 'memory_usage': 5, 'open_files_count': 2,
            'kubernetes_public_ip': 'kubernetes_public_ip', 'private_ip': ['private_ip', 'private_ip'],
            'docker_container_network_mode': 'docker_container_network_mode', 'cloud_account_id': 'cloud_account_id',
            'kubernetes_type': 'kubernetes_type', 'resource_group': 'resource_group', 'docker_image_tag':
            'docker_image_tag', 'kubernetes_labels': 'kubernetes_labels', 'docker_container_ips': ['docker_container_ips',
            'docker_container_ips'], 'docker_image_id': 'docker_image_id', 'timestamp': 'timestamp', 'interface_ips':
            ['interface_ips', 'interface_ips'], 'availability_zone': 'availability_zone', 'is_console_vm': True, 'os': 'os',
            'local_cidr': ['local_cidr', 'local_cidr'], 'node_name': 'node_name', 'threads': 3, 'cloud_provider':
            'cloud_provider', 'docker_container_command': 'docker_container_command', 'agent_running': True, 'uptime': 2,
            'memory_max': 5, 'docker_image_created_at': 'docker_image_created_at', 'kernel_version': 'kernel_version',
            'docker_container_state_human': 'docker_container_state_human', 'docker_image_virtual_size':
            'docker_image_virtual_size', 'kubernetes_ingress_ip': ['kubernetes_ingress_ip', 'kubernetes_ingress_ip'],
            'host_name': 'host_name', 'node_id': 'node_id'}, 'adjacency': ['adjacency', 'adjacency'], 'ids': ['ids', 'ids'],
            'id': 'id', 'label': 'label', 'type': 'type'}}, 'edges': {'key': {'source': 'source', 'target': 'target'}}}

    Attributes:
        edges (ModelGraphResultEdges):
        nodes (ModelGraphResultNodes):
    """

    edges: "ModelGraphResultEdges"
    nodes: "ModelGraphResultNodes"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        edges = self.edges.to_dict()

        nodes = self.nodes.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "edges": edges,
                "nodes": nodes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_graph_result_edges import ModelGraphResultEdges
        from ..models.model_graph_result_nodes import ModelGraphResultNodes

        d = src_dict.copy()
        edges = ModelGraphResultEdges.from_dict(d.pop("edges"))

        nodes = ModelGraphResultNodes.from_dict(d.pop("nodes"))

        model_graph_result = cls(
            edges=edges,
            nodes=nodes,
        )

        model_graph_result.additional_properties = d
        return model_graph_result

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
