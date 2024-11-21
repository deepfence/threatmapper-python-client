import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.postgresql_db_scheduler_last_ran_at import PostgresqlDbSchedulerLastRanAt


T = TypeVar("T", bound="PostgresqlDbScheduler")


@_attrs_define
class PostgresqlDbScheduler:
    """
    Example:
        {'is_enabled': True, 'is_system': True, 'last_ran_at': '{}', 'updated_at': datetime.datetime(2000, 1, 23, 4, 56,
            7, tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'payload': '', 'cron_expr': 'cron_expr',
            'action': 'action', 'created_at': datetime.datetime(2000, 1, 23, 4, 56, 7,
            tzinfo=datetime.timezone(datetime.timedelta(0), '+00:00')), 'description': 'description', 'id': 0, 'status':
            'status'}

    Attributes:
        action (Union[Unset, str]):
        created_at (Union[Unset, datetime.datetime]):
        cron_expr (Union[Unset, str]):
        description (Union[Unset, str]):
        id (Union[Unset, int]):
        is_enabled (Union[Unset, bool]):
        is_system (Union[Unset, bool]):
        last_ran_at (Union[Unset, PostgresqlDbSchedulerLastRanAt]):
        payload (Union[Unset, Any]):
        status (Union[Unset, str]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    action: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    cron_expr: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    is_enabled: Union[Unset, bool] = UNSET
    is_system: Union[Unset, bool] = UNSET
    last_ran_at: Union[Unset, "PostgresqlDbSchedulerLastRanAt"] = UNSET
    payload: Union[Unset, Any] = UNSET
    status: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        cron_expr = self.cron_expr

        description = self.description

        id = self.id

        is_enabled = self.is_enabled

        is_system = self.is_system

        last_ran_at: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_ran_at, Unset):
            last_ran_at = self.last_ran_at.to_dict()

        payload = self.payload

        status = self.status

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if cron_expr is not UNSET:
            field_dict["cron_expr"] = cron_expr
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if is_enabled is not UNSET:
            field_dict["is_enabled"] = is_enabled
        if is_system is not UNSET:
            field_dict["is_system"] = is_system
        if last_ran_at is not UNSET:
            field_dict["last_ran_at"] = last_ran_at
        if payload is not UNSET:
            field_dict["payload"] = payload
        if status is not UNSET:
            field_dict["status"] = status
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.postgresql_db_scheduler_last_ran_at import PostgresqlDbSchedulerLastRanAt

        d = src_dict.copy()
        action = d.pop("action", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        cron_expr = d.pop("cron_expr", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        is_enabled = d.pop("is_enabled", UNSET)

        is_system = d.pop("is_system", UNSET)

        _last_ran_at = d.pop("last_ran_at", UNSET)
        last_ran_at: Union[Unset, PostgresqlDbSchedulerLastRanAt]
        if isinstance(_last_ran_at, Unset):
            last_ran_at = UNSET
        else:
            last_ran_at = PostgresqlDbSchedulerLastRanAt.from_dict(_last_ran_at)

        payload = d.pop("payload", UNSET)

        status = d.pop("status", UNSET)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        postgresql_db_scheduler = cls(
            action=action,
            created_at=created_at,
            cron_expr=cron_expr,
            description=description,
            id=id,
            is_enabled=is_enabled,
            is_system=is_system,
            last_ran_at=last_ran_at,
            payload=payload,
            status=status,
            updated_at=updated_at,
        )

        postgresql_db_scheduler.additional_properties = d
        return postgresql_db_scheduler

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
