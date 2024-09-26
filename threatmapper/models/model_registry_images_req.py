from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_fetch_window import ModelFetchWindow
    from ..models.reporters_fields_filters import ReportersFieldsFilters


T = TypeVar("T", bound="ModelRegistryImagesReq")


@_attrs_define
class ModelRegistryImagesReq:
    """
    Attributes:
        image_filter (ReportersFieldsFilters):
        image_stub_filter (ReportersFieldsFilters):
        registry_id (str):
        window (ModelFetchWindow):
    """

    image_filter: "ReportersFieldsFilters"
    image_stub_filter: "ReportersFieldsFilters"
    registry_id: str
    window: "ModelFetchWindow"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image_filter = self.image_filter.to_dict()

        image_stub_filter = self.image_stub_filter.to_dict()

        registry_id = self.registry_id

        window = self.window.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_filter": image_filter,
                "image_stub_filter": image_stub_filter,
                "registry_id": registry_id,
                "window": window,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_fetch_window import ModelFetchWindow
        from ..models.reporters_fields_filters import ReportersFieldsFilters

        d = src_dict.copy()
        image_filter = ReportersFieldsFilters.from_dict(d.pop("image_filter"))

        image_stub_filter = ReportersFieldsFilters.from_dict(d.pop("image_stub_filter"))

        registry_id = d.pop("registry_id")

        window = ModelFetchWindow.from_dict(d.pop("window"))

        model_registry_images_req = cls(
            image_filter=image_filter,
            image_stub_filter=image_stub_filter,
            registry_id=registry_id,
            window=window,
        )

        model_registry_images_req.additional_properties = d
        return model_registry_images_req

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
