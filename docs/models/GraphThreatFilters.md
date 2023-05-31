# threatmapper.model.graph_threat_filters.GraphThreatFilters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cloud_resource_only** | bool,  | BoolClass,  |  | 
**aws_filter** | [**GraphCloudProviderFilter**](GraphCloudProviderFilter.md) | [**GraphCloudProviderFilter**](GraphCloudProviderFilter.md) |  | 
**gcp_filter** | [**GraphCloudProviderFilter**](GraphCloudProviderFilter.md) | [**GraphCloudProviderFilter**](GraphCloudProviderFilter.md) |  | 
**type** | str,  | str,  |  | must be one of ["all", "vulnerability", "secret", "malware", "compliance", "cloud_compliance", ] 
**azure_filter** | [**GraphCloudProviderFilter**](GraphCloudProviderFilter.md) | [**GraphCloudProviderFilter**](GraphCloudProviderFilter.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

