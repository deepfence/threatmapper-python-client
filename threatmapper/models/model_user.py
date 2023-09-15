from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_user_role import ModelUserRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_user_groups import ModelUserGroups


T = TypeVar("T", bound="ModelUser")


@_attrs_define
class ModelUser:
    """
    Example:
        {'is_active': True, 'role': 'admin', 'company_id': 0, 'role_id': 1, 'groups': {'key': 'groups'}, 'last_name':
            'last_name', 'company': 'company', 'id': 6, 'password_invalidated': True, 'first_name': 'first_name', 'email':
            'email', 'current_user': True}

    Attributes:
        company (str):
        email (str):
        first_name (str):
        last_name (str):
        company_id (Union[Unset, int]):
        current_user (Union[Unset, None, bool]):
        groups (Union[Unset, None, ModelUserGroups]):
        id (Union[Unset, int]):
        is_active (Union[Unset, bool]):
        password_invalidated (Union[Unset, bool]):
        role (Union[Unset, ModelUserRole]):
        role_id (Union[Unset, int]):
    """

    company: str
    email: str
    first_name: str
    last_name: str
    company_id: Union[Unset, int] = UNSET
    current_user: Union[Unset, None, bool] = UNSET
    groups: Union[Unset, None, "ModelUserGroups"] = UNSET
    id: Union[Unset, int] = UNSET
    is_active: Union[Unset, bool] = UNSET
    password_invalidated: Union[Unset, bool] = UNSET
    role: Union[Unset, ModelUserRole] = UNSET
    role_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        company = self.company
        email = self.email
        first_name = self.first_name
        last_name = self.last_name
        company_id = self.company_id
        current_user = self.current_user
        groups: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups.to_dict() if self.groups else None

        id = self.id
        is_active = self.is_active
        password_invalidated = self.password_invalidated
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        role_id = self.role_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company": company,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
            }
        )
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if current_user is not UNSET:
            field_dict["current_user"] = current_user
        if groups is not UNSET:
            field_dict["groups"] = groups
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if password_invalidated is not UNSET:
            field_dict["password_invalidated"] = password_invalidated
        if role is not UNSET:
            field_dict["role"] = role
        if role_id is not UNSET:
            field_dict["role_id"] = role_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.model_user_groups import ModelUserGroups

        d = src_dict.copy()
        company = d.pop("company")

        email = d.pop("email")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        company_id = d.pop("company_id", UNSET)

        current_user = d.pop("current_user", UNSET)

        _groups = d.pop("groups", UNSET)
        groups: Union[Unset, None, ModelUserGroups]
        if _groups is None:
            groups = None
        elif isinstance(_groups, Unset):
            groups = UNSET
        else:
            groups = ModelUserGroups.from_dict(_groups)

        id = d.pop("id", UNSET)

        is_active = d.pop("is_active", UNSET)

        password_invalidated = d.pop("password_invalidated", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, ModelUserRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ModelUserRole(_role)

        role_id = d.pop("role_id", UNSET)

        model_user = cls(
            company=company,
            email=email,
            first_name=first_name,
            last_name=last_name,
            company_id=company_id,
            current_user=current_user,
            groups=groups,
            id=id,
            is_active=is_active,
            password_invalidated=password_invalidated,
            role=role,
            role_id=role_id,
        )

        model_user.additional_properties = d
        return model_user

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
