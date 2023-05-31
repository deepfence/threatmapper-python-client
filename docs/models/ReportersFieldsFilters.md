# threatmapper.model.reporters_fields_filters.ReportersFieldsFilters

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[compare_filter](#compare_filter)** | list, tuple, None,  | tuple, NoneClass,  |  | 
**order_filter** | [**ReportersOrderFilter**](ReportersOrderFilter.md) | [**ReportersOrderFilter**](ReportersOrderFilter.md) |  | 
**contains_filter** | [**ReportersContainsFilter**](ReportersContainsFilter.md) | [**ReportersContainsFilter**](ReportersContainsFilter.md) |  | 
**match_filter** | [**ReportersMatchFilter**](ReportersMatchFilter.md) | [**ReportersMatchFilter**](ReportersMatchFilter.md) |  | 
**not_contains_filter** | [**ReportersContainsFilter**](ReportersContainsFilter.md) | [**ReportersContainsFilter**](ReportersContainsFilter.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# compare_filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReportersCompareFilter**](ReportersCompareFilter.md) | [**ReportersCompareFilter**](ReportersCompareFilter.md) | [**ReportersCompareFilter**](ReportersCompareFilter.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

