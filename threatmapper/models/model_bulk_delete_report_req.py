from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelBulkDeleteReportReq")


@_attrs_define
class ModelBulkDeleteReportReq:
    """
    Attributes:
        report_ids (Union[List[str], None]):
    """

    report_ids: Union[List[str], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        report_ids: Union[List[str], None]
        if isinstance(self.report_ids, list):
            report_ids = self.report_ids

        else:
            report_ids = self.report_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "report_ids": report_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_report_ids(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                report_ids_type_0 = cast(List[str], data)

                return report_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        report_ids = _parse_report_ids(d.pop("report_ids"))

        model_bulk_delete_report_req = cls(
            report_ids=report_ids,
        )

        model_bulk_delete_report_req.additional_properties = d
        return model_bulk_delete_report_req

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
