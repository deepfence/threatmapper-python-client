# threatmapper.model.report_metadata.ReportMetadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**agent_running** | bool,  | BoolClass,  |  | [optional] 
**availability_zone** | str,  | str,  |  | [optional] 
**cloud_provider** | str,  | str,  |  | [optional] 
**cloud_region** | str,  | str,  |  | [optional] 
**cmdline** | str,  | str,  |  | [optional] 
**connection_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**copy_of** | str,  | str,  |  | [optional] 
**cpu_max** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**cpu_usage** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**docker_container_command** | str,  | str,  |  | [optional] 
**docker_container_created** | str,  | str,  |  | [optional] 
**[docker_container_ips](#docker_container_ips)** | list, tuple,  | tuple,  |  | [optional] 
**docker_container_name** | str,  | str,  |  | [optional] 
**docker_container_network_mode** | str,  | str,  |  | [optional] 
**docker_container_networks** | str,  | str,  |  | [optional] 
**docker_container_ports** | str,  | str,  |  | [optional] 
**docker_container_state** | str,  | str,  |  | [optional] 
**docker_container_state_human** | str,  | str,  |  | [optional] 
**docker_env** | str,  | str,  |  | [optional] 
**docker_image_created_at** | str,  | str,  |  | [optional] 
**docker_image_id** | str,  | str,  |  | [optional] 
**docker_image_name** | str,  | str,  |  | [optional] 
**docker_image_name_with_tag** | str,  | str,  |  | [optional] 
**docker_image_size** | str,  | str,  |  | [optional] 
**docker_image_tag** | str,  | str,  |  | [optional] 
**docker_image_virtual_size** | str,  | str,  |  | [optional] 
**docker_label** | str,  | str,  |  | [optional] 
**host_name** | str,  | str,  |  | [optional] 
**instance_id** | str,  | str,  |  | [optional] 
**instance_type** | str,  | str,  |  | [optional] 
**interface_ip_map** | str,  | str,  |  | [optional] 
**[interface_ips](#interface_ips)** | list, tuple,  | tuple,  |  | [optional] 
**[interface_names](#interface_names)** | list, tuple,  | tuple,  |  | [optional] 
**is_console_vm** | bool,  | BoolClass,  |  | [optional] 
**kernel_id** | str,  | str,  |  | [optional] 
**kernel_version** | str,  | str,  |  | [optional] 
**kubernetes_cluster_id** | str,  | str,  |  | [optional] 
**kubernetes_cluster_name** | str,  | str,  |  | [optional] 
**kubernetes_created** | str,  | str,  |  | [optional] 
**[kubernetes_ingress_ip](#kubernetes_ingress_ip)** | list, tuple,  | tuple,  |  | [optional] 
**kubernetes_ip** | str,  | str,  |  | [optional] 
**kubernetes_is_in_host_network** | bool,  | BoolClass,  |  | [optional] 
**kubernetes_labels** | str,  | str,  |  | [optional] 
**kubernetes_namespace** | str,  | str,  |  | [optional] 
**[kubernetes_ports](#kubernetes_ports)** | list, tuple,  | tuple,  |  | [optional] 
**kubernetes_public_ip** | str,  | str,  |  | [optional] 
**kubernetes_state** | str,  | str,  |  | [optional] 
**kubernetes_type** | str,  | str,  |  | [optional] 
**[local_cidr](#local_cidr)** | list, tuple,  | tuple,  |  | [optional] 
**[local_networks](#local_networks)** | list, tuple,  | tuple,  |  | [optional] 
**memory_max** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**memory_usage** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**node_id** | str,  | str,  |  | [optional] 
**node_name** | str,  | str,  |  | [optional] 
**node_type** | str,  | str,  |  | [optional] 
**[open_files](#open_files)** | list, tuple,  | tuple,  |  | [optional] 
**open_files_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**os** | str,  | str,  |  | [optional] 
**pid** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**pod_name** | str,  | str,  |  | [optional] 
**ppid** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[private_ip](#private_ip)** | list, tuple,  | tuple,  |  | [optional] 
**pseudo** | bool,  | BoolClass,  |  | [optional] 
**[public_ip](#public_ip)** | list, tuple,  | tuple,  |  | [optional] 
**resource_group** | str,  | str,  |  | [optional] 
**threads** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**timestamp** | str,  | str,  |  | [optional] 
**uptime** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**[user_defined_tags](#user_defined_tags)** | list, tuple,  | tuple,  |  | [optional] 
**version** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# docker_container_ips

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# interface_ips

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# interface_names

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# kubernetes_ingress_ip

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# kubernetes_ports

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# local_cidr

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# local_networks

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# open_files

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# private_ip

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# public_ip

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# user_defined_tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

