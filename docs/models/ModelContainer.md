# threatmapper.model.model_container.ModelContainer

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vulnerabilities_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**secrets_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**docker_container_state** | str,  | str,  |  | 
**cpu_max** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**memory_usage** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**secret_latest_scan_id** | str,  | str,  |  | 
**docker_container_network_mode** | str,  | str,  |  | 
**vulnerability_latest_scan_id** | str,  | str,  |  | 
**malware_scan_status** | str,  | str,  |  | 
**[docker_container_ips](#docker_container_ips)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**[docker_labels](#docker_labels)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**image** | [**ModelContainerImage**](ModelContainerImage.md) | [**ModelContainerImage**](ModelContainerImage.md) |  | 
**[processes](#processes)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**secret_scan_status** | str,  | str,  |  | 
**docker_container_name** | str,  | str,  |  | 
**docker_container_created** | str,  | str,  |  | 
**malware_latest_scan_id** | str,  | str,  |  | 
**malwares_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**node_name** | str,  | str,  |  | 
**docker_container_networks** | str,  | str,  |  | 
**docker_container_command** | str,  | str,  |  | 
**uptime** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**memory_max** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**docker_container_ports** | str,  | str,  |  | 
**docker_container_state_human** | str,  | str,  |  | 
**cpu_usage** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**vulnerability_scan_status** | str,  | str,  |  | 
**host_name** | str,  | str,  |  | 
**node_id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# docker_container_ips

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# docker_labels

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# processes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelProcess**](ModelProcess.md) | [**ModelProcess**](ModelProcess.md) | [**ModelProcess**](ModelProcess.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

