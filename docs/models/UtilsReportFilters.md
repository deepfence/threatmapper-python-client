# threatmapper.model.utils_report_filters.UtilsReportFilters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**node_type** | str,  | str,  |  | must be one of ["host", "container", "container_image", "linux", "cluster", "aws", "gcp", "azure", ] 
**scan_type** | str,  | str,  |  | must be one of ["vulnerability", "secret", "malware", "compliance", "cloud_compliance", ] 
**advanced_report_filters** | [**UtilsAdvancedReportFilters**](UtilsAdvancedReportFilters.md) | [**UtilsAdvancedReportFilters**](UtilsAdvancedReportFilters.md) |  | [optional] 
**include_dead_nodes** | bool,  | BoolClass,  |  | [optional] 
**scan_id** | str,  | str,  |  | [optional] 
**[severity_or_check_type](#severity_or_check_type)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# severity_or_check_type

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

