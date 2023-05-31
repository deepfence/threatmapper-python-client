# threatmapper.model.model_container_image.ModelContainerImage

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**metadata** | [**ModelMetadata**](ModelMetadata.md) | [**ModelMetadata**](ModelMetadata.md) |  | 
**secret_scan_status** | str,  | str,  |  | 
**vulnerabilities_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**secrets_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**malware_latest_scan_id** | str,  | str,  |  | 
**malwares_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**node_name** | str,  | str,  |  | 
**secret_latest_scan_id** | str,  | str,  |  | 
**vulnerability_latest_scan_id** | str,  | str,  |  | 
**docker_image_created_at** | str,  | str,  |  | 
**docker_image_tag** | str,  | str,  |  | 
**malware_scan_status** | str,  | str,  |  | 
**docker_image_size** | str,  | str,  |  | 
**docker_image_virtual_size** | str,  | str,  |  | 
**[containers](#containers)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**docker_image_id** | str,  | str,  |  | 
**vulnerability_scan_status** | str,  | str,  |  | 
**docker_image_name** | str,  | str,  |  | 
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

