from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_registry_credentials import ModelRegistryCredentials


T = TypeVar("T", bound="ModelLicense")


@_attrs_define
class ModelLicense:
    """
    Example:
        {'end_date': 'end_date', 'no_of_registries': 5, 'notification_threshold_percentage': 2, 'current_hosts': 0,
            'is_active': True, 'license_type': 'license_type', 'notification_threshold_updated_at': 7,
            'registry_credentials': {'registry_url': 'registry_url', 'password': 'password', 'username': 'username'},
            'description': 'description', 'no_of_hosts': 1, 'no_of_images_in_registry': 5, 'message': 'message',
            'deepfence_support_email': 'deepfence_support_email', 'license_email': 'license_email', 'no_of_cloud_accounts':
            6, 'license_email_domain': 'license_email_domain', 'key': 'key', 'start_date': 'start_date'}

    Attributes:
        current_hosts (Union[Unset, int]):
        deepfence_support_email (Union[Unset, str]):
        description (Union[Unset, str]):
        end_date (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        key (Union[Unset, str]):
        license_email (Union[Unset, str]):
        license_email_domain (Union[Unset, str]):
        license_type (Union[Unset, str]):
        message (Union[Unset, str]):
        no_of_cloud_accounts (Union[Unset, int]):
        no_of_hosts (Union[Unset, int]):
        no_of_images_in_registry (Union[Unset, int]):
        no_of_registries (Union[Unset, int]):
        notification_threshold_percentage (Union[Unset, int]):
        notification_threshold_updated_at (Union[Unset, int]):
        registry_credentials (Union[Unset, ModelRegistryCredentials]):  Example: {'registry_url': 'registry_url',
            'password': 'password', 'username': 'username'}.
        start_date (Union[Unset, str]):
    """

    current_hosts: Union[Unset, int] = UNSET
    deepfence_support_email: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    key: Union[Unset, str] = UNSET
    license_email: Union[Unset, str] = UNSET
    license_email_domain: Union[Unset, str] = UNSET
    license_type: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    no_of_cloud_accounts: Union[Unset, int] = UNSET
    no_of_hosts: Union[Unset, int] = UNSET
    no_of_images_in_registry: Union[Unset, int] = UNSET
    no_of_registries: Union[Unset, int] = UNSET
    notification_threshold_percentage: Union[Unset, int] = UNSET
    notification_threshold_updated_at: Union[Unset, int] = UNSET
    registry_credentials: Union[Unset, "ModelRegistryCredentials"] = UNSET
    start_date: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_hosts = self.current_hosts

        deepfence_support_email = self.deepfence_support_email

        description = self.description

        end_date = self.end_date

        is_active = self.is_active

        key = self.key

        license_email = self.license_email

        license_email_domain = self.license_email_domain

        license_type = self.license_type

        message = self.message

        no_of_cloud_accounts = self.no_of_cloud_accounts

        no_of_hosts = self.no_of_hosts

        no_of_images_in_registry = self.no_of_images_in_registry

        no_of_registries = self.no_of_registries

        notification_threshold_percentage = self.notification_threshold_percentage

        notification_threshold_updated_at = self.notification_threshold_updated_at

        registry_credentials: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.registry_credentials, Unset):
            registry_credentials = self.registry_credentials.to_dict()

        start_date = self.start_date

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_hosts is not UNSET:
            field_dict["current_hosts"] = current_hosts
        if deepfence_support_email is not UNSET:
            field_dict["deepfence_support_email"] = deepfence_support_email
        if description is not UNSET:
            field_dict["description"] = description
        if end_date is not UNSET:
            field_dict["end_date"] = end_date
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if key is not UNSET:
            field_dict["key"] = key
        if license_email is not UNSET:
            field_dict["license_email"] = license_email
        if license_email_domain is not UNSET:
            field_dict["license_email_domain"] = license_email_domain
        if license_type is not UNSET:
            field_dict["license_type"] = license_type
        if message is not UNSET:
            field_dict["message"] = message
        if no_of_cloud_accounts is not UNSET:
            field_dict["no_of_cloud_accounts"] = no_of_cloud_accounts
        if no_of_hosts is not UNSET:
            field_dict["no_of_hosts"] = no_of_hosts
        if no_of_images_in_registry is not UNSET:
            field_dict["no_of_images_in_registry"] = no_of_images_in_registry
        if no_of_registries is not UNSET:
            field_dict["no_of_registries"] = no_of_registries
        if notification_threshold_percentage is not UNSET:
            field_dict["notification_threshold_percentage"] = notification_threshold_percentage
        if notification_threshold_updated_at is not UNSET:
            field_dict["notification_threshold_updated_at"] = notification_threshold_updated_at
        if registry_credentials is not UNSET:
            field_dict["registry_credentials"] = registry_credentials
        if start_date is not UNSET:
            field_dict["start_date"] = start_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_registry_credentials import ModelRegistryCredentials

        d = src_dict.copy()
        current_hosts = d.pop("current_hosts", UNSET)

        deepfence_support_email = d.pop("deepfence_support_email", UNSET)

        description = d.pop("description", UNSET)

        end_date = d.pop("end_date", UNSET)

        is_active = d.pop("is_active", UNSET)

        key = d.pop("key", UNSET)

        license_email = d.pop("license_email", UNSET)

        license_email_domain = d.pop("license_email_domain", UNSET)

        license_type = d.pop("license_type", UNSET)

        message = d.pop("message", UNSET)

        no_of_cloud_accounts = d.pop("no_of_cloud_accounts", UNSET)

        no_of_hosts = d.pop("no_of_hosts", UNSET)

        no_of_images_in_registry = d.pop("no_of_images_in_registry", UNSET)

        no_of_registries = d.pop("no_of_registries", UNSET)

        notification_threshold_percentage = d.pop("notification_threshold_percentage", UNSET)

        notification_threshold_updated_at = d.pop("notification_threshold_updated_at", UNSET)

        _registry_credentials = d.pop("registry_credentials", UNSET)
        registry_credentials: Union[Unset, ModelRegistryCredentials]
        if isinstance(_registry_credentials, Unset):
            registry_credentials = UNSET
        else:
            registry_credentials = ModelRegistryCredentials.from_dict(_registry_credentials)

        start_date = d.pop("start_date", UNSET)

        model_license = cls(
            current_hosts=current_hosts,
            deepfence_support_email=deepfence_support_email,
            description=description,
            end_date=end_date,
            is_active=is_active,
            key=key,
            license_email=license_email,
            license_email_domain=license_email_domain,
            license_type=license_type,
            message=message,
            no_of_cloud_accounts=no_of_cloud_accounts,
            no_of_hosts=no_of_hosts,
            no_of_images_in_registry=no_of_images_in_registry,
            no_of_registries=no_of_registries,
            notification_threshold_percentage=notification_threshold_percentage,
            notification_threshold_updated_at=notification_threshold_updated_at,
            registry_credentials=registry_credentials,
            start_date=start_date,
        )

        model_license.additional_properties = d
        return model_license

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
