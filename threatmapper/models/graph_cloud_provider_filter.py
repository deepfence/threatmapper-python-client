from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GraphCloudProviderFilter")


@_attrs_define
class GraphCloudProviderFilter:
    """
    Attributes:
        account_ids (Union[List[str], None]):
    """

    account_ids: Union[List[str], None]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_ids: Union[List[str], None]
        if isinstance(self.account_ids, list):
            account_ids = self.account_ids

        else:
            account_ids = self.account_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_ids": account_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_account_ids(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                account_ids_type_0 = cast(List[str], data)

                return account_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        account_ids = _parse_account_ids(d.pop("account_ids"))

        graph_cloud_provider_filter = cls(
            account_ids=account_ids,
        )

        graph_cloud_provider_filter.additional_properties = d
        return graph_cloud_provider_filter

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
