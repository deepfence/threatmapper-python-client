from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow
    from ..models.search_chained_search_filter import SearchChainedSearchFilter
    from ..models.search_search_filter import SearchSearchFilter


T = TypeVar("T", bound="SearchSearchScanReq")


@_attrs_define
class SearchSearchScanReq:
    """
    Attributes:
        node_filters (SearchSearchFilter):
        scan_filters (SearchSearchFilter):
        window (ModelFetchWindow):
        related_node_filter (Union[Unset, SearchChainedSearchFilter]):
    """

    node_filters: "SearchSearchFilter"
    scan_filters: "SearchSearchFilter"
    window: "ModelFetchWindow"
    related_node_filter: Union[Unset, "SearchChainedSearchFilter"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        node_filters = self.node_filters.to_dict()

        scan_filters = self.scan_filters.to_dict()

        window = self.window.to_dict()

        related_node_filter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.related_node_filter, Unset):
            related_node_filter = self.related_node_filter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "node_filters": node_filters,
                "scan_filters": scan_filters,
                "window": window,
            }
        )
        if related_node_filter is not UNSET:
            field_dict["related_node_filter"] = related_node_filter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow
        from ..models.search_chained_search_filter import SearchChainedSearchFilter
        from ..models.search_search_filter import SearchSearchFilter

        d = src_dict.copy()
        node_filters = SearchSearchFilter.from_dict(d.pop("node_filters"))

        scan_filters = SearchSearchFilter.from_dict(d.pop("scan_filters"))

        window = ModelFetchWindow.from_dict(d.pop("window"))

        _related_node_filter = d.pop("related_node_filter", UNSET)
        related_node_filter: Union[Unset, SearchChainedSearchFilter]
        if isinstance(_related_node_filter, Unset):
            related_node_filter = UNSET
        else:
            related_node_filter = SearchChainedSearchFilter.from_dict(_related_node_filter)

        search_search_scan_req = cls(
            node_filters=node_filters,
            scan_filters=scan_filters,
            window=window,
            related_node_filter=related_node_filter,
        )

        search_search_scan_req.additional_properties = d
        return search_search_scan_req

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
