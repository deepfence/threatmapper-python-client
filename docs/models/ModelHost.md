# threatmapper.model.model_host.ModelHost

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vulnerabilities_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**[public_ip](#public_ip)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**secrets_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**cloud_region** | str,  | str,  |  | 
**[container_images](#container_images)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**cpu_max** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**memory_usage** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**[private_ip](#private_ip)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**secret_latest_scan_id** | str,  | str,  |  | 
**vulnerability_latest_scan_id** | str,  | str,  |  | 
**resource_group** | str,  | str,  |  | 
**malware_scan_status** | str,  | str,  |  | 
**[inbound_connections](#inbound_connections)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**availability_zone** | str,  | str,  |  | 
**is_console_vm** | bool,  | BoolClass,  |  | 
**[processes](#processes)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**secret_scan_status** | str,  | str,  |  | 
**compliance_scan_status** | str,  | str,  |  | 
**[outbound_connections](#outbound_connections)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**os** | str,  | str,  |  | 
**[local_cidr](#local_cidr)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**malware_latest_scan_id** | str,  | str,  |  | 
**malwares_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**node_name** | str,  | str,  |  | 
**cloud_provider** | str,  | str,  |  | 
**agent_running** | bool,  | BoolClass,  |  | 
**version** | str,  | str,  |  | 
**uptime** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**memory_max** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**instance_id** | str,  | str,  |  | 
**kernel_id** | str,  | str,  |  | 
**compliances_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**kernel_version** | str,  | str,  |  | 
**compliance_latest_scan_id** | str,  | str,  |  | 
**[containers](#containers)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**[pods](#pods)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**cpu_usage** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**instance_type** | str,  | str,  |  | 
**vulnerability_scan_status** | str,  | str,  |  | 
**host_name** | str,  | str,  |  | 
**[local_networks](#local_networks)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**node_id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# container_images

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelContainerImage**](ModelContainerImage.md) | [**ModelContainerImage**](ModelContainerImage.md) | [**ModelContainerImage**](ModelContainerImage.md) |  | 

# containers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelContainer**](ModelContainer.md) | [**ModelContainer**](ModelContainer.md) | [**ModelContainer**](ModelContainer.md) |  | 

# inbound_connections

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelConnection**](ModelConnection.md) | [**ModelConnection**](ModelConnection.md) | [**ModelConnection**](ModelConnection.md) |  | 

# local_cidr

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# local_networks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# outbound_connections

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelConnection**](ModelConnection.md) | [**ModelConnection**](ModelConnection.md) | [**ModelConnection**](ModelConnection.md) |  | 

# pods

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelPod**](ModelPod.md) | [**ModelPod**](ModelPod.md) | [**ModelPod**](ModelPod.md) |  | 

# private_ip

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# processes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelProcess**](ModelProcess.md) | [**ModelProcess**](ModelProcess.md) | [**ModelProcess**](ModelProcess.md) |  | 

# public_ip

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

