from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_docs_bad_request_response_error_fields_type_0 import ApiDocsBadRequestResponseErrorFieldsType0
    from ..models.api_docs_bad_request_response_error_index_type_0 import ApiDocsBadRequestResponseErrorIndexType0


T = TypeVar("T", bound="ApiDocsBadRequestResponse")


@_attrs_define
class ApiDocsBadRequestResponse:
    """
    Example:
        {'error_index': {'key': [0, 0]}, 'success': False, 'error_fields': {'key': 'error_fields'}, 'message':
            'message'}

    Attributes:
        error_fields (Union['ApiDocsBadRequestResponseErrorFieldsType0', None, Unset]):
        error_index (Union['ApiDocsBadRequestResponseErrorIndexType0', None, Unset]):
        message (Union[Unset, str]):
        success (Union[Unset, bool]):
    """

    error_fields: Union["ApiDocsBadRequestResponseErrorFieldsType0", None, Unset] = UNSET
    error_index: Union["ApiDocsBadRequestResponseErrorIndexType0", None, Unset] = UNSET
    message: Union[Unset, str] = UNSET
    success: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.api_docs_bad_request_response_error_fields_type_0 import ApiDocsBadRequestResponseErrorFieldsType0
        from ..models.api_docs_bad_request_response_error_index_type_0 import ApiDocsBadRequestResponseErrorIndexType0

        error_fields: Union[Dict[str, Any], None, Unset]
        if isinstance(self.error_fields, Unset):
            error_fields = UNSET
        elif isinstance(self.error_fields, ApiDocsBadRequestResponseErrorFieldsType0):
            error_fields = self.error_fields.to_dict()
        else:
            error_fields = self.error_fields

        error_index: Union[Dict[str, Any], None, Unset]
        if isinstance(self.error_index, Unset):
            error_index = UNSET
        elif isinstance(self.error_index, ApiDocsBadRequestResponseErrorIndexType0):
            error_index = self.error_index.to_dict()
        else:
            error_index = self.error_index

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
        from ..models.api_docs_bad_request_response_error_fields_type_0 import ApiDocsBadRequestResponseErrorFieldsType0
        from ..models.api_docs_bad_request_response_error_index_type_0 import ApiDocsBadRequestResponseErrorIndexType0

        d = src_dict.copy()

        def _parse_error_fields(data: object) -> Union["ApiDocsBadRequestResponseErrorFieldsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_fields_type_0 = ApiDocsBadRequestResponseErrorFieldsType0.from_dict(data)

                return error_fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ApiDocsBadRequestResponseErrorFieldsType0", None, Unset], data)

        error_fields = _parse_error_fields(d.pop("error_fields", UNSET))

        def _parse_error_index(data: object) -> Union["ApiDocsBadRequestResponseErrorIndexType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_index_type_0 = ApiDocsBadRequestResponseErrorIndexType0.from_dict(data)

                return error_index_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ApiDocsBadRequestResponseErrorIndexType0", None, Unset], data)

        error_index = _parse_error_index(d.pop("error_index", UNSET))

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
