from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_scan_info_status import ModelScanInfoStatus

if TYPE_CHECKING:
    from ..models.model_scan_info_severity_counts_type_0 import ModelScanInfoSeverityCountsType0


T = TypeVar("T", bound="ModelScanInfo")


@_attrs_define
class ModelScanInfo:
    """
    Attributes:
        created_at (int):
        node_id (str):
        node_name (str):
        node_type (str):
        scan_id (str):
        severity_counts (Union['ModelScanInfoSeverityCountsType0', None]):
        status (ModelScanInfoStatus):
        status_message (str):
        updated_at (int):
    """

    created_at: int
    node_id: str
    node_name: str
    node_type: str
    scan_id: str
    severity_counts: Union["ModelScanInfoSeverityCountsType0", None]
    status: ModelScanInfoStatus
    status_message: str
    updated_at: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.model_scan_info_severity_counts_type_0 import ModelScanInfoSeverityCountsType0

        created_at = self.created_at

        node_id = self.node_id

        node_name = self.node_name

        node_type = self.node_type

        scan_id = self.scan_id

        severity_counts: Union[Dict[str, Any], None]
        if isinstance(self.severity_counts, ModelScanInfoSeverityCountsType0):
            severity_counts = self.severity_counts.to_dict()
        else:
            severity_counts = self.severity_counts

        status = self.status.value

        status_message = self.status_message

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "node_id": node_id,
                "node_name": node_name,
                "node_type": node_type,
                "scan_id": scan_id,
                "severity_counts": severity_counts,
                "status": status,
                "status_message": status_message,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_scan_info_severity_counts_type_0 import ModelScanInfoSeverityCountsType0

        d = src_dict.copy()
        created_at = d.pop("created_at")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        node_type = d.pop("node_type")

        scan_id = d.pop("scan_id")

        def _parse_severity_counts(data: object) -> Union["ModelScanInfoSeverityCountsType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                severity_counts_type_0 = ModelScanInfoSeverityCountsType0.from_dict(data)

                return severity_counts_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ModelScanInfoSeverityCountsType0", None], data)

        severity_counts = _parse_severity_counts(d.pop("severity_counts"))

        status = ModelScanInfoStatus(d.pop("status"))

        status_message = d.pop("status_message")

        updated_at = d.pop("updated_at")

        model_scan_info = cls(
            created_at=created_at,
            node_id=node_id,
            node_name=node_name,
            node_type=node_type,
            scan_id=scan_id,
            severity_counts=severity_counts,
            status=status,
            status_message=status_message,
            updated_at=updated_at,
        )

        model_scan_info.additional_properties = d
        return model_scan_info

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
