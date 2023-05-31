# threatmapper.model.model_user.ModelUser

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**last_name** | str,  | str,  |  | 
**company** | str,  | str,  |  | 
**first_name** | str,  | str,  |  | 
**email** | str,  | str,  |  | 
**company_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**current_user** | None, bool,  | NoneClass, BoolClass,  |  | [optional] 
**[groups](#groups)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**is_active** | bool,  | BoolClass,  |  | [optional] 
**password_invalidated** | bool,  | BoolClass,  |  | [optional] 
**role** | str,  | str,  |  | [optional] must be one of ["admin", "standard-user", "read-only-user", ] 
**role_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# groups

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

