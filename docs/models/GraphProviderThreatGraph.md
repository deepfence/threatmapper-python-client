# threatmapper.model.graph_provider_threat_graph.GraphProviderThreatGraph

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cloud_compliance_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**secrets_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**[resources](#resources)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**vulnerability_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**compliance_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# resources

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**GraphThreatNodeInfo**](GraphThreatNodeInfo.md) | [**GraphThreatNodeInfo**](GraphThreatNodeInfo.md) | [**GraphThreatNodeInfo**](GraphThreatNodeInfo.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

