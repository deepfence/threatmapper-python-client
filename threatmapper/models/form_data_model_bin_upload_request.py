from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import File

T = TypeVar("T", bound="FormDataModelBinUploadRequest")


@_attrs_define
class FormDataModelBinUploadRequest:
    """
    Attributes:
        tarball (File):
    """

    tarball: File
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tarball = self.tarball.to_tuple()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tarball": tarball,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        tarball = self.tarball.to_tuple()

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "tarball": tarball,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tarball = File(payload=BytesIO(d.pop("tarball")))

        form_data_model_bin_upload_request = cls(
            tarball=tarball,
        )

        form_data_model_bin_upload_request.additional_properties = d
        return form_data_model_bin_upload_request

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
