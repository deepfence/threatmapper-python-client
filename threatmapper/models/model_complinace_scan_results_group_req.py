from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="ModelComplinaceScanResultsGroupReq")


@_attrs_define
class ModelComplinaceScanResultsGroupReq:
    """
    Attributes:
        fields_filter (ReportersFieldsFilters):
        scan_id (str):
    """

    fields_filter: "ReportersFieldsFilters"
    scan_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fields_filter = self.fields_filter.to_dict()

        scan_id = self.scan_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields_filter": fields_filter,
                "scan_id": scan_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = src_dict.copy()
        fields_filter = ReportersFieldsFilters.from_dict(d.pop("fields_filter"))

        scan_id = d.pop("scan_id")

        model_complinace_scan_results_group_req = cls(
            fields_filter=fields_filter,
            scan_id=scan_id,
        )

        model_complinace_scan_results_group_req.additional_properties = d
        return model_complinace_scan_results_group_req

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
