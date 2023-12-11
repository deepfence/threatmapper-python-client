from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_secret import ModelSecret


T = TypeVar("T", bound="ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelSecret")


@_attrs_define
class ModelScanCompareResGithubComDeepfenceThreatMapperDeepfenceServerModelSecret:
    """
    Example:
        {'new': [{'full_filename': 'full_filename', 'level': 'level', 'masked': True, 'part': 'part',
            'relative_ending_index': 0, 'starting_index': 5, 'resources': [{'node_type': 'node_type', 'name': 'name',
            'host_name': 'host_name', 'node_id': 'node_id'}, {'node_type': 'node_type', 'name': 'name', 'host_name':
            'host_name', 'node_id': 'node_id'}], 'signature_to_match': 'signature_to_match', 'rule_id': 1, 'score':
            5.962133916683182, 'matched_content': 'matched_content', 'updated_at': 2, 'name': 'name',
            'relative_starting_index': 6, 'node_id': 'node_id'}, {'full_filename': 'full_filename', 'level': 'level',
            'masked': True, 'part': 'part', 'relative_ending_index': 0, 'starting_index': 5, 'resources': [{'node_type':
            'node_type', 'name': 'name', 'host_name': 'host_name', 'node_id': 'node_id'}, {'node_type': 'node_type', 'name':
            'name', 'host_name': 'host_name', 'node_id': 'node_id'}], 'signature_to_match': 'signature_to_match', 'rule_id':
            1, 'score': 5.962133916683182, 'matched_content': 'matched_content', 'updated_at': 2, 'name': 'name',
            'relative_starting_index': 6, 'node_id': 'node_id'}]}

    Attributes:
        new (Optional[List['ModelSecret']]):
    """

    new: Optional[List["ModelSecret"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if self.new is None:
            new = None
        else:
            new = []
            for new_item_data in self.new:
                new_item = new_item_data.to_dict()

                new.append(new_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "new": new,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_secret import ModelSecret

        d = src_dict.copy()
        new = []
        _new = d.pop("new")
        for new_item_data in _new or []:
            new_item = ModelSecret.from_dict(new_item_data)

            new.append(new_item)

        model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_secret = cls(
            new=new,
        )

        model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_secret.additional_properties = (
            d
        )
        return model_scan_compare_res_github_com_deepfence_threat_mapper_deepfence_server_model_secret

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
