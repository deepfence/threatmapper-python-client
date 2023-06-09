# coding: utf-8

"""
    Deepfence ThreatMapper

    Deepfence Runtime API provides programmatic control over Deepfence microservice securing your container, kubernetes and cloud deployments. The API abstracts away underlying infrastructure details like cloud provider,  container distros, container orchestrator and type of deployment. This is one uniform API to manage and control security alerts, policies and response to alerts for microservices running anywhere i.e. managed pure greenfield container deployments or a mix of containers, VMs and serverless paradigms like AWS Fargate.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: community@deepfence.io
    Generated by: https://openapi-generator.tech
"""

from threatmapper.paths.deepfence_auth_token.post import AuthToken
from threatmapper.paths.deepfence_auth_token_refresh.post import AuthTokenRefresh
from threatmapper.paths.deepfence_user_login.post import Login
from threatmapper.paths.deepfence_user_logout.post import Logout


class AuthenticationApi(
    AuthToken,
    AuthTokenRefresh,
    Login,
    Logout,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
