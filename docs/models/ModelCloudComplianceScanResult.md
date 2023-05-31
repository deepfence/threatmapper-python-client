# threatmapper.model.model_cloud_compliance_scan_result.ModelCloudComplianceScanResult

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[benchmark_type](#benchmark_type)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**docker_container_name** | str,  | str,  |  | 
**kubernetes_cluster_name** | str,  | str,  |  | 
**node_name** | str,  | str,  |  | 
**created_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**[compliances](#compliances)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**compliance_percentage** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**node_type** | str,  | str,  |  | 
**updated_at** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer
**scan_id** | str,  | str,  |  | 
**[status_counts](#status_counts)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 
**docker_image_name** | str,  | str,  |  | 
**host_name** | str,  | str,  |  | 
**node_id** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# benchmark_type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# compliances

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ModelCloudCompliance**](ModelCloudCompliance.md) | [**ModelCloudCompliance**](ModelCloudCompliance.md) | [**ModelCloudCompliance**](ModelCloudCompliance.md) |  | 

# status_counts

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | decimal.Decimal, int,  | decimal.Decimal,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

