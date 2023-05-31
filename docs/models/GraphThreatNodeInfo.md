# threatmapper.model.graph_threat_node_info.GraphThreatNodeInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cloud_compliance_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**node_type** | str,  | str,  |  | 
**[nodes](#nodes)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**secrets_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**id** | str,  | str,  |  | 
**label** | str,  | str,  |  | 
**vulnerability_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**[attack_path](#attack_path)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**compliance_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attack_path

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# nodes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**GraphNodeInfo**](GraphNodeInfo.md) | [**GraphNodeInfo**](GraphNodeInfo.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

