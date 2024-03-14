from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="ModelScanCompareReq")


@_attrs_define
class ModelScanCompareReq:
    """
    Attributes:
        base_scan_id (str):
        fields_filter (ReportersFieldsFilters):
        to_scan_id (str):
        window (ModelFetchWindow):
    """

    base_scan_id: str
    fields_filter: "ReportersFieldsFilters"
    to_scan_id: str
    window: "ModelFetchWindow"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        base_scan_id = self.base_scan_id

        fields_filter = self.fields_filter.to_dict()

        to_scan_id = self.to_scan_id

        window = self.window.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base_scan_id": base_scan_id,
                "fields_filter": fields_filter,
                "to_scan_id": to_scan_id,
                "window": window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = src_dict.copy()
        base_scan_id = d.pop("base_scan_id")

        fields_filter = ReportersFieldsFilters.from_dict(d.pop("fields_filter"))

        to_scan_id = d.pop("to_scan_id")

        window = ModelFetchWindow.from_dict(d.pop("window"))

        model_scan_compare_req = cls(
            base_scan_id=base_scan_id,
            fields_filter=fields_filter,
            to_scan_id=to_scan_id,
            window=window,
        )

        model_scan_compare_req.additional_properties = d
        return model_scan_compare_req

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
