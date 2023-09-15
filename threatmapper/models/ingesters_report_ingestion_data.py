from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.ingesters_report_ingestion_data_container_batch_item import (
        IngestersReportIngestionDataContainerBatchItem,
    )
    from ..models.ingesters_report_ingestion_data_container_edges_batch_item import (
        IngestersReportIngestionDataContainerEdgesBatchItem,
    )
    from ..models.ingesters_report_ingestion_data_container_image_batch_item import (
        IngestersReportIngestionDataContainerImageBatchItem,
    )
    from ..models.ingesters_report_ingestion_data_container_image_edge_batch_item import (
        IngestersReportIngestionDataContainerImageEdgeBatchItem,
    )
    from ..models.ingesters_report_ingestion_data_container_process_edge_batch_item import (
        IngestersReportIngestionDataContainerProcessEdgeBatchItem,
    )
    from ..models.ingesters_report_ingestion_data_endpoint_edges_batch_item import (
        IngestersReportIngestionDataEndpointEdgesBatchItem,
    )
    from ..models.ingesters_report_ingestion_data_host_batch_item import IngestersReportIngestionDataHostBatchItem
    from ..models.ingesters_report_ingestion_data_hosts_item import IngestersReportIngestionDataHostsItem
    from ..models.ingesters_report_ingestion_data_kubernetes_cluster_batch_item import (
        IngestersReportIngestionDataKubernetesClusterBatchItem,
    )
    from ..models.ingesters_report_ingestion_data_kubernetes_cluster_edge_batch_item import (
        IngestersReportIngestionDataKubernetesClusterEdgeBatchItem,
    )
    from ..models.ingesters_report_ingestion_data_pod_batch_item import IngestersReportIngestionDataPodBatchItem
    from ..models.ingesters_report_ingestion_data_pod_edges_batch_item import (
        IngestersReportIngestionDataPodEdgesBatchItem,
    )
    from ..models.ingesters_report_ingestion_data_pod_host_edges_batch_item import (
        IngestersReportIngestionDataPodHostEdgesBatchItem,
    )
    from ..models.ingesters_report_ingestion_data_process_batch_item import IngestersReportIngestionDataProcessBatchItem
    from ..models.ingesters_report_ingestion_data_process_edges_batch_item import (
        IngestersReportIngestionDataProcessEdgesBatchItem,
    )


T = TypeVar("T", bound="IngestersReportIngestionData")


@_attrs_define
class IngestersReportIngestionData:
    """
    Example:
        {'hosts': [{'key': ''}, {'key': ''}], 'host_batch': [{'key': ''}, {'key': ''}], 'kubernetes_cluster_edge_batch':
            [{'key': ''}, {'key': ''}], 'process_batch': [{'key': ''}, {'key': ''}], 'container_image_edge_batch': [{'key':
            ''}, {'key': ''}], 'num_merged': 0, 'container_process_edge_batch': [{'key': ''}, {'key': ''}], 'pod_batch':
            [{'key': ''}, {'key': ''}], 'process_edges_batch': [{'key': ''}, {'key': ''}], 'container_edges_batch': [{'key':
            ''}, {'key': ''}], 'container_batch': [{'key': ''}, {'key': ''}], 'container_image_batch': [{'key': ''}, {'key':
            ''}], 'kubernetes_cluster_batch': [{'key': ''}, {'key': ''}], 'pod_edges_batch': [{'key': ''}, {'key': ''}],
            'endpoint_edges_batch': [{'key': ''}, {'key': ''}], 'pod_host_edges_batch': [{'key': ''}, {'key': ''}]}

    Attributes:
        num_merged (int):
        container_batch (Optional[List['IngestersReportIngestionDataContainerBatchItem']]):
        container_edges_batch (Optional[List['IngestersReportIngestionDataContainerEdgesBatchItem']]):
        container_image_batch (Optional[List['IngestersReportIngestionDataContainerImageBatchItem']]):
        container_image_edge_batch (Optional[List['IngestersReportIngestionDataContainerImageEdgeBatchItem']]):
        container_process_edge_batch (Optional[List['IngestersReportIngestionDataContainerProcessEdgeBatchItem']]):
        endpoint_edges_batch (Optional[List['IngestersReportIngestionDataEndpointEdgesBatchItem']]):
        host_batch (Optional[List['IngestersReportIngestionDataHostBatchItem']]):
        hosts (Optional[List['IngestersReportIngestionDataHostsItem']]):
        kubernetes_cluster_batch (Optional[List['IngestersReportIngestionDataKubernetesClusterBatchItem']]):
        kubernetes_cluster_edge_batch (Optional[List['IngestersReportIngestionDataKubernetesClusterEdgeBatchItem']]):
        pod_batch (Optional[List['IngestersReportIngestionDataPodBatchItem']]):
        pod_edges_batch (Optional[List['IngestersReportIngestionDataPodEdgesBatchItem']]):
        pod_host_edges_batch (Optional[List['IngestersReportIngestionDataPodHostEdgesBatchItem']]):
        process_batch (Optional[List['IngestersReportIngestionDataProcessBatchItem']]):
        process_edges_batch (Optional[List['IngestersReportIngestionDataProcessEdgesBatchItem']]):
    """

    num_merged: int
    container_batch: Optional[List["IngestersReportIngestionDataContainerBatchItem"]]
    container_edges_batch: Optional[List["IngestersReportIngestionDataContainerEdgesBatchItem"]]
    container_image_batch: Optional[List["IngestersReportIngestionDataContainerImageBatchItem"]]
    container_image_edge_batch: Optional[List["IngestersReportIngestionDataContainerImageEdgeBatchItem"]]
    container_process_edge_batch: Optional[List["IngestersReportIngestionDataContainerProcessEdgeBatchItem"]]
    endpoint_edges_batch: Optional[List["IngestersReportIngestionDataEndpointEdgesBatchItem"]]
    host_batch: Optional[List["IngestersReportIngestionDataHostBatchItem"]]
    hosts: Optional[List["IngestersReportIngestionDataHostsItem"]]
    kubernetes_cluster_batch: Optional[List["IngestersReportIngestionDataKubernetesClusterBatchItem"]]
    kubernetes_cluster_edge_batch: Optional[List["IngestersReportIngestionDataKubernetesClusterEdgeBatchItem"]]
    pod_batch: Optional[List["IngestersReportIngestionDataPodBatchItem"]]
    pod_edges_batch: Optional[List["IngestersReportIngestionDataPodEdgesBatchItem"]]
    pod_host_edges_batch: Optional[List["IngestersReportIngestionDataPodHostEdgesBatchItem"]]
    process_batch: Optional[List["IngestersReportIngestionDataProcessBatchItem"]]
    process_edges_batch: Optional[List["IngestersReportIngestionDataProcessEdgesBatchItem"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_merged = self.num_merged
        if self.container_batch is None:
            container_batch = None
        else:
            container_batch = []
            for container_batch_item_data in self.container_batch:
                container_batch_item = container_batch_item_data.to_dict()

                container_batch.append(container_batch_item)

        if self.container_edges_batch is None:
            container_edges_batch = None
        else:
            container_edges_batch = []
            for container_edges_batch_item_data in self.container_edges_batch:
                container_edges_batch_item = container_edges_batch_item_data.to_dict()

                container_edges_batch.append(container_edges_batch_item)

        if self.container_image_batch is None:
            container_image_batch = None
        else:
            container_image_batch = []
            for container_image_batch_item_data in self.container_image_batch:
                container_image_batch_item = container_image_batch_item_data.to_dict()

                container_image_batch.append(container_image_batch_item)

        if self.container_image_edge_batch is None:
            container_image_edge_batch = None
        else:
            container_image_edge_batch = []
            for container_image_edge_batch_item_data in self.container_image_edge_batch:
                container_image_edge_batch_item = container_image_edge_batch_item_data.to_dict()

                container_image_edge_batch.append(container_image_edge_batch_item)

        if self.container_process_edge_batch is None:
            container_process_edge_batch = None
        else:
            container_process_edge_batch = []
            for container_process_edge_batch_item_data in self.container_process_edge_batch:
                container_process_edge_batch_item = container_process_edge_batch_item_data.to_dict()

                container_process_edge_batch.append(container_process_edge_batch_item)

        if self.endpoint_edges_batch is None:
            endpoint_edges_batch = None
        else:
            endpoint_edges_batch = []
            for endpoint_edges_batch_item_data in self.endpoint_edges_batch:
                endpoint_edges_batch_item = endpoint_edges_batch_item_data.to_dict()

                endpoint_edges_batch.append(endpoint_edges_batch_item)

        if self.host_batch is None:
            host_batch = None
        else:
            host_batch = []
            for host_batch_item_data in self.host_batch:
                host_batch_item = host_batch_item_data.to_dict()

                host_batch.append(host_batch_item)

        if self.hosts is None:
            hosts = None
        else:
            hosts = []
            for hosts_item_data in self.hosts:
                hosts_item = hosts_item_data.to_dict()

                hosts.append(hosts_item)

        if self.kubernetes_cluster_batch is None:
            kubernetes_cluster_batch = None
        else:
            kubernetes_cluster_batch = []
            for kubernetes_cluster_batch_item_data in self.kubernetes_cluster_batch:
                kubernetes_cluster_batch_item = kubernetes_cluster_batch_item_data.to_dict()

                kubernetes_cluster_batch.append(kubernetes_cluster_batch_item)

        if self.kubernetes_cluster_edge_batch is None:
            kubernetes_cluster_edge_batch = None
        else:
            kubernetes_cluster_edge_batch = []
            for kubernetes_cluster_edge_batch_item_data in self.kubernetes_cluster_edge_batch:
                kubernetes_cluster_edge_batch_item = kubernetes_cluster_edge_batch_item_data.to_dict()

                kubernetes_cluster_edge_batch.append(kubernetes_cluster_edge_batch_item)

        if self.pod_batch is None:
            pod_batch = None
        else:
            pod_batch = []
            for pod_batch_item_data in self.pod_batch:
                pod_batch_item = pod_batch_item_data.to_dict()

                pod_batch.append(pod_batch_item)

        if self.pod_edges_batch is None:
            pod_edges_batch = None
        else:
            pod_edges_batch = []
            for pod_edges_batch_item_data in self.pod_edges_batch:
                pod_edges_batch_item = pod_edges_batch_item_data.to_dict()

                pod_edges_batch.append(pod_edges_batch_item)

        if self.pod_host_edges_batch is None:
            pod_host_edges_batch = None
        else:
            pod_host_edges_batch = []
            for pod_host_edges_batch_item_data in self.pod_host_edges_batch:
                pod_host_edges_batch_item = pod_host_edges_batch_item_data.to_dict()

                pod_host_edges_batch.append(pod_host_edges_batch_item)

        if self.process_batch is None:
            process_batch = None
        else:
            process_batch = []
            for process_batch_item_data in self.process_batch:
                process_batch_item = process_batch_item_data.to_dict()

                process_batch.append(process_batch_item)

        if self.process_edges_batch is None:
            process_edges_batch = None
        else:
            process_edges_batch = []
            for process_edges_batch_item_data in self.process_edges_batch:
                process_edges_batch_item = process_edges_batch_item_data.to_dict()

                process_edges_batch.append(process_edges_batch_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "num_merged": num_merged,
                "container_batch": container_batch,
                "container_edges_batch": container_edges_batch,
                "container_image_batch": container_image_batch,
                "container_image_edge_batch": container_image_edge_batch,
                "container_process_edge_batch": container_process_edge_batch,
                "endpoint_edges_batch": endpoint_edges_batch,
                "host_batch": host_batch,
                "hosts": hosts,
                "kubernetes_cluster_batch": kubernetes_cluster_batch,
                "kubernetes_cluster_edge_batch": kubernetes_cluster_edge_batch,
                "pod_batch": pod_batch,
                "pod_edges_batch": pod_edges_batch,
                "pod_host_edges_batch": pod_host_edges_batch,
                "process_batch": process_batch,
                "process_edges_batch": process_edges_batch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ingesters_report_ingestion_data_container_batch_item import (
            IngestersReportIngestionDataContainerBatchItem,
        )
        from ..models.ingesters_report_ingestion_data_container_edges_batch_item import (
            IngestersReportIngestionDataContainerEdgesBatchItem,
        )
        from ..models.ingesters_report_ingestion_data_container_image_batch_item import (
            IngestersReportIngestionDataContainerImageBatchItem,
        )
        from ..models.ingesters_report_ingestion_data_container_image_edge_batch_item import (
            IngestersReportIngestionDataContainerImageEdgeBatchItem,
        )
        from ..models.ingesters_report_ingestion_data_container_process_edge_batch_item import (
            IngestersReportIngestionDataContainerProcessEdgeBatchItem,
        )
        from ..models.ingesters_report_ingestion_data_endpoint_edges_batch_item import (
            IngestersReportIngestionDataEndpointEdgesBatchItem,
        )
        from ..models.ingesters_report_ingestion_data_host_batch_item import IngestersReportIngestionDataHostBatchItem
        from ..models.ingesters_report_ingestion_data_hosts_item import IngestersReportIngestionDataHostsItem
        from ..models.ingesters_report_ingestion_data_kubernetes_cluster_batch_item import (
            IngestersReportIngestionDataKubernetesClusterBatchItem,
        )
        from ..models.ingesters_report_ingestion_data_kubernetes_cluster_edge_batch_item import (
            IngestersReportIngestionDataKubernetesClusterEdgeBatchItem,
        )
        from ..models.ingesters_report_ingestion_data_pod_batch_item import IngestersReportIngestionDataPodBatchItem
        from ..models.ingesters_report_ingestion_data_pod_edges_batch_item import (
            IngestersReportIngestionDataPodEdgesBatchItem,
        )
        from ..models.ingesters_report_ingestion_data_pod_host_edges_batch_item import (
            IngestersReportIngestionDataPodHostEdgesBatchItem,
        )
        from ..models.ingesters_report_ingestion_data_process_batch_item import (
            IngestersReportIngestionDataProcessBatchItem,
        )
        from ..models.ingesters_report_ingestion_data_process_edges_batch_item import (
            IngestersReportIngestionDataProcessEdgesBatchItem,
        )

        d = src_dict.copy()
        num_merged = d.pop("num_merged")

        container_batch = []
        _container_batch = d.pop("container_batch")
        for container_batch_item_data in _container_batch or []:
            container_batch_item = IngestersReportIngestionDataContainerBatchItem.from_dict(container_batch_item_data)

            container_batch.append(container_batch_item)

        container_edges_batch = []
        _container_edges_batch = d.pop("container_edges_batch")
        for container_edges_batch_item_data in _container_edges_batch or []:
            container_edges_batch_item = IngestersReportIngestionDataContainerEdgesBatchItem.from_dict(
                container_edges_batch_item_data
            )

            container_edges_batch.append(container_edges_batch_item)

        container_image_batch = []
        _container_image_batch = d.pop("container_image_batch")
        for container_image_batch_item_data in _container_image_batch or []:
            container_image_batch_item = IngestersReportIngestionDataContainerImageBatchItem.from_dict(
                container_image_batch_item_data
            )

            container_image_batch.append(container_image_batch_item)

        container_image_edge_batch = []
        _container_image_edge_batch = d.pop("container_image_edge_batch")
        for container_image_edge_batch_item_data in _container_image_edge_batch or []:
            container_image_edge_batch_item = IngestersReportIngestionDataContainerImageEdgeBatchItem.from_dict(
                container_image_edge_batch_item_data
            )

            container_image_edge_batch.append(container_image_edge_batch_item)

        container_process_edge_batch = []
        _container_process_edge_batch = d.pop("container_process_edge_batch")
        for container_process_edge_batch_item_data in _container_process_edge_batch or []:
            container_process_edge_batch_item = IngestersReportIngestionDataContainerProcessEdgeBatchItem.from_dict(
                container_process_edge_batch_item_data
            )

            container_process_edge_batch.append(container_process_edge_batch_item)

        endpoint_edges_batch = []
        _endpoint_edges_batch = d.pop("endpoint_edges_batch")
        for endpoint_edges_batch_item_data in _endpoint_edges_batch or []:
            endpoint_edges_batch_item = IngestersReportIngestionDataEndpointEdgesBatchItem.from_dict(
                endpoint_edges_batch_item_data
            )

            endpoint_edges_batch.append(endpoint_edges_batch_item)

        host_batch = []
        _host_batch = d.pop("host_batch")
        for host_batch_item_data in _host_batch or []:
            host_batch_item = IngestersReportIngestionDataHostBatchItem.from_dict(host_batch_item_data)

            host_batch.append(host_batch_item)

        hosts = []
        _hosts = d.pop("hosts")
        for hosts_item_data in _hosts or []:
            hosts_item = IngestersReportIngestionDataHostsItem.from_dict(hosts_item_data)

            hosts.append(hosts_item)

        kubernetes_cluster_batch = []
        _kubernetes_cluster_batch = d.pop("kubernetes_cluster_batch")
        for kubernetes_cluster_batch_item_data in _kubernetes_cluster_batch or []:
            kubernetes_cluster_batch_item = IngestersReportIngestionDataKubernetesClusterBatchItem.from_dict(
                kubernetes_cluster_batch_item_data
            )

            kubernetes_cluster_batch.append(kubernetes_cluster_batch_item)

        kubernetes_cluster_edge_batch = []
        _kubernetes_cluster_edge_batch = d.pop("kubernetes_cluster_edge_batch")
        for kubernetes_cluster_edge_batch_item_data in _kubernetes_cluster_edge_batch or []:
            kubernetes_cluster_edge_batch_item = IngestersReportIngestionDataKubernetesClusterEdgeBatchItem.from_dict(
                kubernetes_cluster_edge_batch_item_data
            )

            kubernetes_cluster_edge_batch.append(kubernetes_cluster_edge_batch_item)

        pod_batch = []
        _pod_batch = d.pop("pod_batch")
        for pod_batch_item_data in _pod_batch or []:
            pod_batch_item = IngestersReportIngestionDataPodBatchItem.from_dict(pod_batch_item_data)

            pod_batch.append(pod_batch_item)

        pod_edges_batch = []
        _pod_edges_batch = d.pop("pod_edges_batch")
        for pod_edges_batch_item_data in _pod_edges_batch or []:
            pod_edges_batch_item = IngestersReportIngestionDataPodEdgesBatchItem.from_dict(pod_edges_batch_item_data)

            pod_edges_batch.append(pod_edges_batch_item)

        pod_host_edges_batch = []
        _pod_host_edges_batch = d.pop("pod_host_edges_batch")
        for pod_host_edges_batch_item_data in _pod_host_edges_batch or []:
            pod_host_edges_batch_item = IngestersReportIngestionDataPodHostEdgesBatchItem.from_dict(
                pod_host_edges_batch_item_data
            )

            pod_host_edges_batch.append(pod_host_edges_batch_item)

        process_batch = []
        _process_batch = d.pop("process_batch")
        for process_batch_item_data in _process_batch or []:
            process_batch_item = IngestersReportIngestionDataProcessBatchItem.from_dict(process_batch_item_data)

            process_batch.append(process_batch_item)

        process_edges_batch = []
        _process_edges_batch = d.pop("process_edges_batch")
        for process_edges_batch_item_data in _process_edges_batch or []:
            process_edges_batch_item = IngestersReportIngestionDataProcessEdgesBatchItem.from_dict(
                process_edges_batch_item_data
            )

            process_edges_batch.append(process_edges_batch_item)

        ingesters_report_ingestion_data = cls(
            num_merged=num_merged,
            container_batch=container_batch,
            container_edges_batch=container_edges_batch,
            container_image_batch=container_image_batch,
            container_image_edge_batch=container_image_edge_batch,
            container_process_edge_batch=container_process_edge_batch,
            endpoint_edges_batch=endpoint_edges_batch,
            host_batch=host_batch,
            hosts=hosts,
            kubernetes_cluster_batch=kubernetes_cluster_batch,
            kubernetes_cluster_edge_batch=kubernetes_cluster_edge_batch,
            pod_batch=pod_batch,
            pod_edges_batch=pod_edges_batch,
            pod_host_edges_batch=pod_host_edges_batch,
            process_batch=process_batch,
            process_edges_batch=process_edges_batch,
        )

        ingesters_report_ingestion_data.additional_properties = d
        return ingesters_report_ingestion_data

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
