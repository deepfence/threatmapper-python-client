from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_container_image import ModelContainerImage


T = TypeVar("T", bound="ModelRegistryAccount")


@_attrs_define
class ModelRegistryAccount:
    """
    Attributes:
        container_images (Union[List['ModelContainerImage'], None]):
        name (str):
        node_id (str):
        registry_type (str):
        syncing (bool):
    """

    container_images: Union[List["ModelContainerImage"], None]
    name: str
    node_id: str
    registry_type: str
    syncing: bool
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        container_images: Union[List[Dict[str, Any]], None]
        if isinstance(self.container_images, list):
            container_images = []
            for container_images_type_0_item_data in self.container_images:
                container_images_type_0_item = container_images_type_0_item_data.to_dict()
                container_images.append(container_images_type_0_item)

        else:
            container_images = self.container_images

        name = self.name

        node_id = self.node_id

        registry_type = self.registry_type

        syncing = self.syncing

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "container_images": container_images,
                "name": name,
                "node_id": node_id,
                "registry_type": registry_type,
                "syncing": syncing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_container_image import ModelContainerImage

        d = src_dict.copy()

        def _parse_container_images(data: object) -> Union[List["ModelContainerImage"], None]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                container_images_type_0 = []
                _container_images_type_0 = data
                for container_images_type_0_item_data in _container_images_type_0:
                    container_images_type_0_item = ModelContainerImage.from_dict(container_images_type_0_item_data)

                    container_images_type_0.append(container_images_type_0_item)

                return container_images_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ModelContainerImage"], None], data)

        container_images = _parse_container_images(d.pop("container_images"))

        name = d.pop("name")

        node_id = d.pop("node_id")

        registry_type = d.pop("registry_type")

        syncing = d.pop("syncing")

        model_registry_account = cls(
            container_images=container_images,
            name=name,
            node_id=node_id,
            registry_type=registry_type,
            syncing=syncing,
        )

        model_registry_account.additional_properties = d
        return model_registry_account

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
