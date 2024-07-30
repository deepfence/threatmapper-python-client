from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_scan_results_action_request_scan_type import ModelScanResultsActionRequestScanType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelScanResultsActionRequest")


@_attrs_define
class ModelScanResultsActionRequest:
    """
    Example:
        {'notify_individual': True, 'result_ids': ['result_ids', 'result_ids'], 'scan_type': 'SecretScan', 'scan_id':
            'scan_id', 'integration_ids': [0, 0]}

    Attributes:
        result_ids (Union[List[str], None]):
        scan_id (str):
        scan_type (ModelScanResultsActionRequestScanType):
        integration_ids (Union[List[int], None, Unset]):
        notify_individual (Union[Unset, bool]):
    """

    result_ids: Union[List[str], None]
    scan_id: str
    scan_type: ModelScanResultsActionRequestScanType
    integration_ids: Union[List[int], None, Unset] = UNSET
    notify_individual: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result_ids: Union[List[str], None]
        if isinstance(self.result_ids, list):
            result_ids = self.result_ids

        else:
            result_ids = self.result_ids

        scan_id = self.scan_id

        scan_type = self.scan_type.value

        integration_ids: Union[List[int], None, Unset]
        if isinstance(self.integration_ids, Unset):
            integration_ids = UNSET
        elif isinstance(self.integration_ids, list):
            integration_ids = self.integration_ids

        else:
            integration_ids = self.integration_ids

        notify_individual = self.notify_individual

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result_ids": result_ids,
                "scan_id": scan_id,
                "scan_type": scan_type,
            }
        )
        if integration_ids is not UNSET:
            field_dict["integration_ids"] = integration_ids
        if notify_individual is not UNSET:
            field_dict["notify_individual"] = notify_individual

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_result_ids(data: object) -> Union[List[str], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                result_ids_type_0 = cast(List[str], data)

                return result_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None], data)

        result_ids = _parse_result_ids(d.pop("result_ids"))

        scan_id = d.pop("scan_id")

        scan_type = ModelScanResultsActionRequestScanType(d.pop("scan_type"))

        def _parse_integration_ids(data: object) -> Union[List[int], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                integration_ids_type_0 = cast(List[int], data)

                return integration_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[int], None, Unset], data)

        integration_ids = _parse_integration_ids(d.pop("integration_ids", UNSET))

        notify_individual = d.pop("notify_individual", UNSET)

        model_scan_results_action_request = cls(
            result_ids=result_ids,
            scan_id=scan_id,
            scan_type=scan_type,
            integration_ids=integration_ids,
            notify_individual=notify_individual,
        )

        model_scan_results_action_request.additional_properties = d
        return model_scan_results_action_request

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
