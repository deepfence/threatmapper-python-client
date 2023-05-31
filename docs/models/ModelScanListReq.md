# threatmapper.model.model_scan_list_req.ModelScanListReq

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**window** | [**ModelFetchWindow**](ModelFetchWindow.md) | [**ModelFetchWindow**](ModelFetchWindow.md) |  | 
**fields_filter** | [**ReportersFieldsFilters**](ReportersFieldsFilters.md) | [**ReportersFieldsFilters**](ReportersFieldsFilters.md) |  | 
**[node_ids](#node_ids)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# node_ids

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelNodeIdentifier**](ModelNodeIdentifier.md) | [**ModelNodeIdentifier**](ModelNodeIdentifier.md) | [**ModelNodeIdentifier**](ModelNodeIdentifier.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

