from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_docs_bad_request_response_error_fields import ApiDocsBadRequestResponseErrorFields
    from ..models.api_docs_bad_request_response_error_index import ApiDocsBadRequestResponseErrorIndex


T = TypeVar("T", bound="ApiDocsBadRequestResponse")


@_attrs_define
class ApiDocsBadRequestResponse:
    """
    Attributes:
        error_fields (Union[Unset, None, ApiDocsBadRequestResponseErrorFields]):
        error_index (Union[Unset, None, ApiDocsBadRequestResponseErrorIndex]):
        message (Union[Unset, str]):
        success (Union[Unset, bool]):
    """

    error_fields: Union[Unset, None, "ApiDocsBadRequestResponseErrorFields"] = UNSET
    error_index: Union[Unset, None, "ApiDocsBadRequestResponseErrorIndex"] = UNSET
    message: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_fields: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.error_fields, Unset):
            error_fields = self.error_fields.to_dict() if self.error_fields else None

        error_index: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.error_index, Unset):
            error_index = self.error_index.to_dict() if self.error_index else None

        message = self.message
        success = self.success

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_fields is not UNSET:
            field_dict["error_fields"] = error_fields
        if error_index is not UNSET:
            field_dict["error_index"] = error_index
        if message is not UNSET:
            field_dict["message"] = message
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_docs_bad_request_response_error_fields import ApiDocsBadRequestResponseErrorFields
        from ..models.api_docs_bad_request_response_error_index import ApiDocsBadRequestResponseErrorIndex

        d = src_dict.copy()
        _error_fields = d.pop("error_fields", UNSET)
        error_fields: Union[Unset, None, ApiDocsBadRequestResponseErrorFields]
        if _error_fields is None:
            error_fields = None
        elif isinstance(_error_fields, Unset):
            error_fields = UNSET
        else:
            error_fields = ApiDocsBadRequestResponseErrorFields.from_dict(_error_fields)

        _error_index = d.pop("error_index", UNSET)
        error_index: Union[Unset, None, ApiDocsBadRequestResponseErrorIndex]
        if _error_index is None:
            error_index = None
        elif isinstance(_error_index, Unset):
            error_index = UNSET
        else:
            error_index = ApiDocsBadRequestResponseErrorIndex.from_dict(_error_index)

        message = d.pop("message", UNSET)

        success = d.pop("success", UNSET)

        api_docs_bad_request_response = cls(
            error_fields=error_fields,
            error_index=error_index,
            message=message,
            success=success,
        )

        api_docs_bad_request_response.additional_properties = d
        return api_docs_bad_request_response

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
