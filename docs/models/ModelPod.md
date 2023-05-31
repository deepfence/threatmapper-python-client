# threatmapper.model.model_pod.ModelPod

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**kubernetes_ip** | str,  | str,  |  | 
**[processes](#processes)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**kubernetes_cluster_id** | str,  | str,  |  | 
**kubernetes_cluster_name** | str,  | str,  |  | 
**kubernetes_state** | str,  | str,  |  | 
**node_name** | str,  | str,  |  | 
**kubernetes_created** | str,  | str,  |  | 
**pod_name** | str,  | str,  |  | 
**kubernetes_namespace** | str,  | str,  |  | 
**kubernetes_is_in_host_network** | bool,  | BoolClass,  |  | 
**[kubernetes_labels](#kubernetes_labels)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**[containers](#containers)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**host_name** | str,  | str,  |  | 
**node_id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# containers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelContainer**](ModelContainer.md) | [**ModelContainer**](ModelContainer.md) | [**ModelContainer**](ModelContainer.md) |  | 

# kubernetes_labels

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

