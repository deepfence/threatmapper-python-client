# threatmapper.model.model_cloud_node_account_register_resp_data.ModelCloudNodeAccountRegisterRespData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[cloudtrail_trails](#cloudtrail_trails)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**refresh** | str,  | str,  |  | [optional] 
**[scans](#scans)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cloudtrail_trails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelCloudNodeCloudtrailTrail**](ModelCloudNodeCloudtrailTrail.md) | [**ModelCloudNodeCloudtrailTrail**](ModelCloudNodeCloudtrailTrail.md) | [**ModelCloudNodeCloudtrailTrail**](ModelCloudNodeCloudtrailTrail.md) |  | 

# scans

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**ModelCloudComplianceScanDetails**](ModelCloudComplianceScanDetails.md) | [**ModelCloudComplianceScanDetails**](ModelCloudComplianceScanDetails.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

