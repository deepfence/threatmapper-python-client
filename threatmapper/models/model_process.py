from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ModelProcess")


@_attrs_define
class ModelProcess:
    """
    Example:
        {'memory_max': 9, 'cmdline': 'cmdline', 'cpu_max': 2.3021358869347655, 'node_name': 'node_name', 'memory_usage':
            3, 'open_files_count': 2, 'threads': 1, 'pid': 4, 'cpu_usage': 7.061401241503109, 'node_id': 'node_id', 'ppid':
            7}

    Attributes:
        cmdline (str):
        cpu_max (float):
        cpu_usage (float):
        memory_max (int):
        memory_usage (int):
        node_id (str):
        node_name (str):
        open_files_count (int):
        pid (int):
        ppid (int):
        threads (int):
    """

    cmdline: str
    cpu_max: float
    cpu_usage: float
    memory_max: int
    memory_usage: int
    node_id: str
    node_name: str
    open_files_count: int
    pid: int
    ppid: int
    threads: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cmdline = self.cmdline
        cpu_max = self.cpu_max
        cpu_usage = self.cpu_usage
        memory_max = self.memory_max
        memory_usage = self.memory_usage
        node_id = self.node_id
        node_name = self.node_name
        open_files_count = self.open_files_count
        pid = self.pid
        ppid = self.ppid
        threads = self.threads

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cmdline": cmdline,
                "cpu_max": cpu_max,
                "cpu_usage": cpu_usage,
                "memory_max": memory_max,
                "memory_usage": memory_usage,
                "node_id": node_id,
                "node_name": node_name,
                "open_files_count": open_files_count,
                "pid": pid,
                "ppid": ppid,
                "threads": threads,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cmdline = d.pop("cmdline")

        cpu_max = d.pop("cpu_max")

        cpu_usage = d.pop("cpu_usage")

        memory_max = d.pop("memory_max")

        memory_usage = d.pop("memory_usage")

        node_id = d.pop("node_id")

        node_name = d.pop("node_name")

        open_files_count = d.pop("open_files_count")

        pid = d.pop("pid")

        ppid = d.pop("ppid")

        threads = d.pop("threads")

        model_process = cls(
            cmdline=cmdline,
            cpu_max=cpu_max,
            cpu_usage=cpu_usage,
            memory_max=memory_max,
            memory_usage=memory_usage,
            node_id=node_id,
            node_name=node_name,
            open_files_count=open_files_count,
            pid=pid,
            ppid=ppid,
            threads=threads,
        )

        model_process.additional_properties = d
        return model_process

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
