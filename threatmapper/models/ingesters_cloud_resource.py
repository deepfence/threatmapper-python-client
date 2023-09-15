from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IngestersCloudResource")


@_attrs_define
class IngestersCloudResource:
    """
    Example:
        {'iam_instance_profile_arn': 'iam_instance_profile_arn', 'allow_blob_public_access': True, 'ingress_settings':
            'ingress_settings', 'vpc_id': 'vpc_id', 'event_notification_configuration': '', 'ip_configuration': '',
            'access_level': 'access_level', 'path': 'path', 'connectivity': 'connectivity', 'policy_std': '',
            'target_health_descriptions': '', 'iam_policy': '', 'action': 'action', 'private_ip_address':
            'private_ip_address', 'id': 'id', 'create_date': 'create_date', 'resource_vpc_config': '', 'inline_policies':
            '', 'restrict_public_buckets': True, 'db_cluster_identifier': 'db_cluster_identifier', 'group': 'group',
            'target_group_arn': 'target_group_arn', 'ignore_public_acls': True, 'storage_account_name':
            'storage_account_name', 'service_name': 'service_name', 'instance_profile_arns': '', 'users': '',
            'network_interfaces': '', 'tags': '', 'security_groups': '', 'task_arn': 'task_arn', 'block_public_acls': True,
            'organization_master_account_email': 'organization_master_account_email', 'instance_id': 'instance_id',
            'public_access': 'public_access', 'task_definition': '', 'user_id': 'user_id', 'organization_id':
            'organization_id', 'name': 'name', 'resources_vpc_config': '', 'attached_policy_arns': '',
            'task_definition_arn': 'task_definition_arn', 'containers': '', 'region': 'region', 'container_definitions': '',
            'instance_type': 'instance_type', 'scheme': 'scheme', 'instances': '', 'network_mode': 'network_mode',
            'is_egress': True, 'description': 'description', 'privilege': 'privilege', 'network_configuration': '',
            'public_network_access': 'public_network_access', 'vpc_options': '', 'vpc_security_group_ids': '', 'arn': 'arn',
            'private_dns_name': 'private_dns_name', 'policy': '', 'public_ips': '', 'cluster_name': 'cluster_name',
            'cluster_arn': 'cluster_arn', 'public_ip_address': 'public_ip_address', 'cidr_ipv4': 'cidr_ipv4', 'last_status':
            'last_status', 'groups': '', 'user-groups': '', 'cloud_provider': 'cloud_provider', 'vpc_security_groups': '',
            'block_public_policy': True, 'account_id': 'account_id', 'iam_instance_profile_id': 'iam_instance_profile_id',
            'group_id': 'group_id', 'organization_master_account_arn': 'organization_master_account_arn', 'resource_id':
            'resource_id', 'bucket_policy_is_public': True, 'host_name': 'host_name'}

    Attributes:
        access_level (Union[Unset, str]):
        account_id (Union[Unset, str]):
        action (Union[Unset, str]):
        allow_blob_public_access (Union[Unset, bool]):
        arn (Union[Unset, str]):
        attached_policy_arns (Union[Unset, Any]):
        block_public_acls (Union[Unset, bool]):
        block_public_policy (Union[Unset, bool]):
        bucket_policy_is_public (Union[Unset, bool]):
        cidr_ipv4 (Union[Unset, str]):
        cloud_provider (Union[Unset, str]):
        cluster_arn (Union[Unset, str]):
        cluster_name (Union[Unset, str]):
        connectivity (Union[Unset, str]):
        container_definitions (Union[Unset, Any]):
        containers (Union[Unset, Any]):
        create_date (Union[Unset, str]):
        db_cluster_identifier (Union[Unset, str]):
        description (Union[Unset, str]):
        event_notification_configuration (Union[Unset, Any]):
        group (Union[Unset, str]):
        group_id (Union[Unset, str]):
        groups (Union[Unset, Any]):
        host_name (Union[Unset, str]):
        iam_instance_profile_arn (Union[Unset, str]):
        iam_instance_profile_id (Union[Unset, str]):
        iam_policy (Union[Unset, Any]):
        id (Union[Unset, str]):
        ignore_public_acls (Union[Unset, bool]):
        ingress_settings (Union[Unset, str]):
        inline_policies (Union[Unset, Any]):
        instance_id (Union[Unset, str]):
        instance_profile_arns (Union[Unset, Any]):
        instance_type (Union[Unset, str]):
        instances (Union[Unset, Any]):
        ip_configuration (Union[Unset, Any]):
        is_egress (Union[Unset, bool]):
        last_status (Union[Unset, str]):
        name (Union[Unset, str]):
        network_configuration (Union[Unset, Any]):
        network_interfaces (Union[Unset, Any]):
        network_mode (Union[Unset, str]):
        organization_id (Union[Unset, str]):
        organization_master_account_arn (Union[Unset, str]):
        organization_master_account_email (Union[Unset, str]):
        path (Union[Unset, str]):
        policy (Union[Unset, Any]):
        policy_std (Union[Unset, Any]):
        private_dns_name (Union[Unset, str]):
        private_ip_address (Union[Unset, str]):
        privilege (Union[Unset, str]):
        public_access (Union[Unset, str]):
        public_ip_address (Union[Unset, str]):
        public_ips (Union[Unset, Any]):
        public_network_access (Union[Unset, str]):
        region (Union[Unset, str]):
        resource_id (Union[Unset, str]):
        resource_vpc_config (Union[Unset, Any]):
        resources_vpc_config (Union[Unset, Any]):
        restrict_public_buckets (Union[Unset, bool]):
        scheme (Union[Unset, str]):
        security_groups (Union[Unset, Any]):
        service_name (Union[Unset, str]):
        storage_account_name (Union[Unset, str]):
        tags (Union[Unset, Any]):
        target_group_arn (Union[Unset, str]):
        target_health_descriptions (Union[Unset, Any]):
        task_arn (Union[Unset, str]):
        task_definition (Union[Unset, Any]):
        task_definition_arn (Union[Unset, str]):
        user_groups (Union[Unset, Any]):
        user_id (Union[Unset, str]):
        users (Union[Unset, Any]):
        vpc_id (Union[Unset, str]):
        vpc_options (Union[Unset, Any]):
        vpc_security_group_ids (Union[Unset, Any]):
        vpc_security_groups (Union[Unset, Any]):
    """

    access_level: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    action: Union[Unset, str] = UNSET
    allow_blob_public_access: Union[Unset, bool] = UNSET
    arn: Union[Unset, str] = UNSET
    attached_policy_arns: Union[Unset, Any] = UNSET
    block_public_acls: Union[Unset, bool] = UNSET
    block_public_policy: Union[Unset, bool] = UNSET
    bucket_policy_is_public: Union[Unset, bool] = UNSET
    cidr_ipv4: Union[Unset, str] = UNSET
    cloud_provider: Union[Unset, str] = UNSET
    cluster_arn: Union[Unset, str] = UNSET
    cluster_name: Union[Unset, str] = UNSET
    connectivity: Union[Unset, str] = UNSET
    container_definitions: Union[Unset, Any] = UNSET
    containers: Union[Unset, Any] = UNSET
    create_date: Union[Unset, str] = UNSET
    db_cluster_identifier: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    event_notification_configuration: Union[Unset, Any] = UNSET
    group: Union[Unset, str] = UNSET
    group_id: Union[Unset, str] = UNSET
    groups: Union[Unset, Any] = UNSET
    host_name: Union[Unset, str] = UNSET
    iam_instance_profile_arn: Union[Unset, str] = UNSET
    iam_instance_profile_id: Union[Unset, str] = UNSET
    iam_policy: Union[Unset, Any] = UNSET
    id: Union[Unset, str] = UNSET
    ignore_public_acls: Union[Unset, bool] = UNSET
    ingress_settings: Union[Unset, str] = UNSET
    inline_policies: Union[Unset, Any] = UNSET
    instance_id: Union[Unset, str] = UNSET
    instance_profile_arns: Union[Unset, Any] = UNSET
    instance_type: Union[Unset, str] = UNSET
    instances: Union[Unset, Any] = UNSET
    ip_configuration: Union[Unset, Any] = UNSET
    is_egress: Union[Unset, bool] = UNSET
    last_status: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    network_configuration: Union[Unset, Any] = UNSET
    network_interfaces: Union[Unset, Any] = UNSET
    network_mode: Union[Unset, str] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization_master_account_arn: Union[Unset, str] = UNSET
    organization_master_account_email: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    policy: Union[Unset, Any] = UNSET
    policy_std: Union[Unset, Any] = UNSET
    private_dns_name: Union[Unset, str] = UNSET
    private_ip_address: Union[Unset, str] = UNSET
    privilege: Union[Unset, str] = UNSET
    public_access: Union[Unset, str] = UNSET
    public_ip_address: Union[Unset, str] = UNSET
    public_ips: Union[Unset, Any] = UNSET
    public_network_access: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    resource_id: Union[Unset, str] = UNSET
    resource_vpc_config: Union[Unset, Any] = UNSET
    resources_vpc_config: Union[Unset, Any] = UNSET
    restrict_public_buckets: Union[Unset, bool] = UNSET
    scheme: Union[Unset, str] = UNSET
    security_groups: Union[Unset, Any] = UNSET
    service_name: Union[Unset, str] = UNSET
    storage_account_name: Union[Unset, str] = UNSET
    tags: Union[Unset, Any] = UNSET
    target_group_arn: Union[Unset, str] = UNSET
    target_health_descriptions: Union[Unset, Any] = UNSET
    task_arn: Union[Unset, str] = UNSET
    task_definition: Union[Unset, Any] = UNSET
    task_definition_arn: Union[Unset, str] = UNSET
    user_groups: Union[Unset, Any] = UNSET
    user_id: Union[Unset, str] = UNSET
    users: Union[Unset, Any] = UNSET
    vpc_id: Union[Unset, str] = UNSET
    vpc_options: Union[Unset, Any] = UNSET
    vpc_security_group_ids: Union[Unset, Any] = UNSET
    vpc_security_groups: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_level = self.access_level
        account_id = self.account_id
        action = self.action
        allow_blob_public_access = self.allow_blob_public_access
        arn = self.arn
        attached_policy_arns = self.attached_policy_arns
        block_public_acls = self.block_public_acls
        block_public_policy = self.block_public_policy
        bucket_policy_is_public = self.bucket_policy_is_public
        cidr_ipv4 = self.cidr_ipv4
        cloud_provider = self.cloud_provider
        cluster_arn = self.cluster_arn
        cluster_name = self.cluster_name
        connectivity = self.connectivity
        container_definitions = self.container_definitions
        containers = self.containers
        create_date = self.create_date
        db_cluster_identifier = self.db_cluster_identifier
        description = self.description
        event_notification_configuration = self.event_notification_configuration
        group = self.group
        group_id = self.group_id
        groups = self.groups
        host_name = self.host_name
        iam_instance_profile_arn = self.iam_instance_profile_arn
        iam_instance_profile_id = self.iam_instance_profile_id
        iam_policy = self.iam_policy
        id = self.id
        ignore_public_acls = self.ignore_public_acls
        ingress_settings = self.ingress_settings
        inline_policies = self.inline_policies
        instance_id = self.instance_id
        instance_profile_arns = self.instance_profile_arns
        instance_type = self.instance_type
        instances = self.instances
        ip_configuration = self.ip_configuration
        is_egress = self.is_egress
        last_status = self.last_status
        name = self.name
        network_configuration = self.network_configuration
        network_interfaces = self.network_interfaces
        network_mode = self.network_mode
        organization_id = self.organization_id
        organization_master_account_arn = self.organization_master_account_arn
        organization_master_account_email = self.organization_master_account_email
        path = self.path
        policy = self.policy
        policy_std = self.policy_std
        private_dns_name = self.private_dns_name
        private_ip_address = self.private_ip_address
        privilege = self.privilege
        public_access = self.public_access
        public_ip_address = self.public_ip_address
        public_ips = self.public_ips
        public_network_access = self.public_network_access
        region = self.region
        resource_id = self.resource_id
        resource_vpc_config = self.resource_vpc_config
        resources_vpc_config = self.resources_vpc_config
        restrict_public_buckets = self.restrict_public_buckets
        scheme = self.scheme
        security_groups = self.security_groups
        service_name = self.service_name
        storage_account_name = self.storage_account_name
        tags = self.tags
        target_group_arn = self.target_group_arn
        target_health_descriptions = self.target_health_descriptions
        task_arn = self.task_arn
        task_definition = self.task_definition
        task_definition_arn = self.task_definition_arn
        user_groups = self.user_groups
        user_id = self.user_id
        users = self.users
        vpc_id = self.vpc_id
        vpc_options = self.vpc_options
        vpc_security_group_ids = self.vpc_security_group_ids
        vpc_security_groups = self.vpc_security_groups

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_level is not UNSET:
            field_dict["access_level"] = access_level
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if action is not UNSET:
            field_dict["action"] = action
        if allow_blob_public_access is not UNSET:
            field_dict["allow_blob_public_access"] = allow_blob_public_access
        if arn is not UNSET:
            field_dict["arn"] = arn
        if attached_policy_arns is not UNSET:
            field_dict["attached_policy_arns"] = attached_policy_arns
        if block_public_acls is not UNSET:
            field_dict["block_public_acls"] = block_public_acls
        if block_public_policy is not UNSET:
            field_dict["block_public_policy"] = block_public_policy
        if bucket_policy_is_public is not UNSET:
            field_dict["bucket_policy_is_public"] = bucket_policy_is_public
        if cidr_ipv4 is not UNSET:
            field_dict["cidr_ipv4"] = cidr_ipv4
        if cloud_provider is not UNSET:
            field_dict["cloud_provider"] = cloud_provider
        if cluster_arn is not UNSET:
            field_dict["cluster_arn"] = cluster_arn
        if cluster_name is not UNSET:
            field_dict["cluster_name"] = cluster_name
        if connectivity is not UNSET:
            field_dict["connectivity"] = connectivity
        if container_definitions is not UNSET:
            field_dict["container_definitions"] = container_definitions
        if containers is not UNSET:
            field_dict["containers"] = containers
        if create_date is not UNSET:
            field_dict["create_date"] = create_date
        if db_cluster_identifier is not UNSET:
            field_dict["db_cluster_identifier"] = db_cluster_identifier
        if description is not UNSET:
            field_dict["description"] = description
        if event_notification_configuration is not UNSET:
            field_dict["event_notification_configuration"] = event_notification_configuration
        if group is not UNSET:
            field_dict["group"] = group
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if groups is not UNSET:
            field_dict["groups"] = groups
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if iam_instance_profile_arn is not UNSET:
            field_dict["iam_instance_profile_arn"] = iam_instance_profile_arn
        if iam_instance_profile_id is not UNSET:
            field_dict["iam_instance_profile_id"] = iam_instance_profile_id
        if iam_policy is not UNSET:
            field_dict["iam_policy"] = iam_policy
        if id is not UNSET:
            field_dict["id"] = id
        if ignore_public_acls is not UNSET:
            field_dict["ignore_public_acls"] = ignore_public_acls
        if ingress_settings is not UNSET:
            field_dict["ingress_settings"] = ingress_settings
        if inline_policies is not UNSET:
            field_dict["inline_policies"] = inline_policies
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if instance_profile_arns is not UNSET:
            field_dict["instance_profile_arns"] = instance_profile_arns
        if instance_type is not UNSET:
            field_dict["instance_type"] = instance_type
        if instances is not UNSET:
            field_dict["instances"] = instances
        if ip_configuration is not UNSET:
            field_dict["ip_configuration"] = ip_configuration
        if is_egress is not UNSET:
            field_dict["is_egress"] = is_egress
        if last_status is not UNSET:
            field_dict["last_status"] = last_status
        if name is not UNSET:
            field_dict["name"] = name
        if network_configuration is not UNSET:
            field_dict["network_configuration"] = network_configuration
        if network_interfaces is not UNSET:
            field_dict["network_interfaces"] = network_interfaces
        if network_mode is not UNSET:
            field_dict["network_mode"] = network_mode
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if organization_master_account_arn is not UNSET:
            field_dict["organization_master_account_arn"] = organization_master_account_arn
        if organization_master_account_email is not UNSET:
            field_dict["organization_master_account_email"] = organization_master_account_email
        if path is not UNSET:
            field_dict["path"] = path
        if policy is not UNSET:
            field_dict["policy"] = policy
        if policy_std is not UNSET:
            field_dict["policy_std"] = policy_std
        if private_dns_name is not UNSET:
            field_dict["private_dns_name"] = private_dns_name
        if private_ip_address is not UNSET:
            field_dict["private_ip_address"] = private_ip_address
        if privilege is not UNSET:
            field_dict["privilege"] = privilege
        if public_access is not UNSET:
            field_dict["public_access"] = public_access
        if public_ip_address is not UNSET:
            field_dict["public_ip_address"] = public_ip_address
        if public_ips is not UNSET:
            field_dict["public_ips"] = public_ips
        if public_network_access is not UNSET:
            field_dict["public_network_access"] = public_network_access
        if region is not UNSET:
            field_dict["region"] = region
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if resource_vpc_config is not UNSET:
            field_dict["resource_vpc_config"] = resource_vpc_config
        if resources_vpc_config is not UNSET:
            field_dict["resources_vpc_config"] = resources_vpc_config
        if restrict_public_buckets is not UNSET:
            field_dict["restrict_public_buckets"] = restrict_public_buckets
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if security_groups is not UNSET:
            field_dict["security_groups"] = security_groups
        if service_name is not UNSET:
            field_dict["service_name"] = service_name
        if storage_account_name is not UNSET:
            field_dict["storage_account_name"] = storage_account_name
        if tags is not UNSET:
            field_dict["tags"] = tags
        if target_group_arn is not UNSET:
            field_dict["target_group_arn"] = target_group_arn
        if target_health_descriptions is not UNSET:
            field_dict["target_health_descriptions"] = target_health_descriptions
        if task_arn is not UNSET:
            field_dict["task_arn"] = task_arn
        if task_definition is not UNSET:
            field_dict["task_definition"] = task_definition
        if task_definition_arn is not UNSET:
            field_dict["task_definition_arn"] = task_definition_arn
        if user_groups is not UNSET:
            field_dict["user-groups"] = user_groups
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if users is not UNSET:
            field_dict["users"] = users
        if vpc_id is not UNSET:
            field_dict["vpc_id"] = vpc_id
        if vpc_options is not UNSET:
            field_dict["vpc_options"] = vpc_options
        if vpc_security_group_ids is not UNSET:
            field_dict["vpc_security_group_ids"] = vpc_security_group_ids
        if vpc_security_groups is not UNSET:
            field_dict["vpc_security_groups"] = vpc_security_groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        access_level = d.pop("access_level", UNSET)

        account_id = d.pop("account_id", UNSET)

        action = d.pop("action", UNSET)

        allow_blob_public_access = d.pop("allow_blob_public_access", UNSET)

        arn = d.pop("arn", UNSET)

        attached_policy_arns = d.pop("attached_policy_arns", UNSET)

        block_public_acls = d.pop("block_public_acls", UNSET)

        block_public_policy = d.pop("block_public_policy", UNSET)

        bucket_policy_is_public = d.pop("bucket_policy_is_public", UNSET)

        cidr_ipv4 = d.pop("cidr_ipv4", UNSET)

        cloud_provider = d.pop("cloud_provider", UNSET)

        cluster_arn = d.pop("cluster_arn", UNSET)

        cluster_name = d.pop("cluster_name", UNSET)

        connectivity = d.pop("connectivity", UNSET)

        container_definitions = d.pop("container_definitions", UNSET)

        containers = d.pop("containers", UNSET)

        create_date = d.pop("create_date", UNSET)

        db_cluster_identifier = d.pop("db_cluster_identifier", UNSET)

        description = d.pop("description", UNSET)

        event_notification_configuration = d.pop("event_notification_configuration", UNSET)

        group = d.pop("group", UNSET)

        group_id = d.pop("group_id", UNSET)

        groups = d.pop("groups", UNSET)

        host_name = d.pop("host_name", UNSET)

        iam_instance_profile_arn = d.pop("iam_instance_profile_arn", UNSET)

        iam_instance_profile_id = d.pop("iam_instance_profile_id", UNSET)

        iam_policy = d.pop("iam_policy", UNSET)

        id = d.pop("id", UNSET)

        ignore_public_acls = d.pop("ignore_public_acls", UNSET)

        ingress_settings = d.pop("ingress_settings", UNSET)

        inline_policies = d.pop("inline_policies", UNSET)

        instance_id = d.pop("instance_id", UNSET)

        instance_profile_arns = d.pop("instance_profile_arns", UNSET)

        instance_type = d.pop("instance_type", UNSET)

        instances = d.pop("instances", UNSET)

        ip_configuration = d.pop("ip_configuration", UNSET)

        is_egress = d.pop("is_egress", UNSET)

        last_status = d.pop("last_status", UNSET)

        name = d.pop("name", UNSET)

        network_configuration = d.pop("network_configuration", UNSET)

        network_interfaces = d.pop("network_interfaces", UNSET)

        network_mode = d.pop("network_mode", UNSET)

        organization_id = d.pop("organization_id", UNSET)

        organization_master_account_arn = d.pop("organization_master_account_arn", UNSET)

        organization_master_account_email = d.pop("organization_master_account_email", UNSET)

        path = d.pop("path", UNSET)

        policy = d.pop("policy", UNSET)

        policy_std = d.pop("policy_std", UNSET)

        private_dns_name = d.pop("private_dns_name", UNSET)

        private_ip_address = d.pop("private_ip_address", UNSET)

        privilege = d.pop("privilege", UNSET)

        public_access = d.pop("public_access", UNSET)

        public_ip_address = d.pop("public_ip_address", UNSET)

        public_ips = d.pop("public_ips", UNSET)

        public_network_access = d.pop("public_network_access", UNSET)

        region = d.pop("region", UNSET)

        resource_id = d.pop("resource_id", UNSET)

        resource_vpc_config = d.pop("resource_vpc_config", UNSET)

        resources_vpc_config = d.pop("resources_vpc_config", UNSET)

        restrict_public_buckets = d.pop("restrict_public_buckets", UNSET)

        scheme = d.pop("scheme", UNSET)

        security_groups = d.pop("security_groups", UNSET)

        service_name = d.pop("service_name", UNSET)

        storage_account_name = d.pop("storage_account_name", UNSET)

        tags = d.pop("tags", UNSET)

        target_group_arn = d.pop("target_group_arn", UNSET)

        target_health_descriptions = d.pop("target_health_descriptions", UNSET)

        task_arn = d.pop("task_arn", UNSET)

        task_definition = d.pop("task_definition", UNSET)

        task_definition_arn = d.pop("task_definition_arn", UNSET)

        user_groups = d.pop("user-groups", UNSET)

        user_id = d.pop("user_id", UNSET)

        users = d.pop("users", UNSET)

        vpc_id = d.pop("vpc_id", UNSET)

        vpc_options = d.pop("vpc_options", UNSET)

        vpc_security_group_ids = d.pop("vpc_security_group_ids", UNSET)

        vpc_security_groups = d.pop("vpc_security_groups", UNSET)

        ingesters_cloud_resource = cls(
            access_level=access_level,
            account_id=account_id,
            action=action,
            allow_blob_public_access=allow_blob_public_access,
            arn=arn,
            attached_policy_arns=attached_policy_arns,
            block_public_acls=block_public_acls,
            block_public_policy=block_public_policy,
            bucket_policy_is_public=bucket_policy_is_public,
            cidr_ipv4=cidr_ipv4,
            cloud_provider=cloud_provider,
            cluster_arn=cluster_arn,
            cluster_name=cluster_name,
            connectivity=connectivity,
            container_definitions=container_definitions,
            containers=containers,
            create_date=create_date,
            db_cluster_identifier=db_cluster_identifier,
            description=description,
            event_notification_configuration=event_notification_configuration,
            group=group,
            group_id=group_id,
            groups=groups,
            host_name=host_name,
            iam_instance_profile_arn=iam_instance_profile_arn,
            iam_instance_profile_id=iam_instance_profile_id,
            iam_policy=iam_policy,
            id=id,
            ignore_public_acls=ignore_public_acls,
            ingress_settings=ingress_settings,
            inline_policies=inline_policies,
            instance_id=instance_id,
            instance_profile_arns=instance_profile_arns,
            instance_type=instance_type,
            instances=instances,
            ip_configuration=ip_configuration,
            is_egress=is_egress,
            last_status=last_status,
            name=name,
            network_configuration=network_configuration,
            network_interfaces=network_interfaces,
            network_mode=network_mode,
            organization_id=organization_id,
            organization_master_account_arn=organization_master_account_arn,
            organization_master_account_email=organization_master_account_email,
            path=path,
            policy=policy,
            policy_std=policy_std,
            private_dns_name=private_dns_name,
            private_ip_address=private_ip_address,
            privilege=privilege,
            public_access=public_access,
            public_ip_address=public_ip_address,
            public_ips=public_ips,
            public_network_access=public_network_access,
            region=region,
            resource_id=resource_id,
            resource_vpc_config=resource_vpc_config,
            resources_vpc_config=resources_vpc_config,
            restrict_public_buckets=restrict_public_buckets,
            scheme=scheme,
            security_groups=security_groups,
            service_name=service_name,
            storage_account_name=storage_account_name,
            tags=tags,
            target_group_arn=target_group_arn,
            target_health_descriptions=target_health_descriptions,
            task_arn=task_arn,
            task_definition=task_definition,
            task_definition_arn=task_definition_arn,
            user_groups=user_groups,
            user_id=user_id,
            users=users,
            vpc_id=vpc_id,
            vpc_options=vpc_options,
            vpc_security_group_ids=vpc_security_group_ids,
            vpc_security_groups=vpc_security_groups,
        )

        ingesters_cloud_resource.additional_properties = d
        return ingesters_cloud_resource

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
