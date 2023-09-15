from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.model_generate_report_req import ModelGenerateReportReq
from ...models.model_generate_report_resp import ModelGenerateReportResp
from ...types import Response


def _get_kwargs(
    *,
    json_body: ModelGenerateReportReq,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/deepfence/reports",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGenerateReportResp]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ModelGenerateReportResp.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ApiDocsBadRequestResponse.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ApiDocsFailureResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ApiDocsFailureResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGenerateReportResp]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ModelGenerateReportReq,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGenerateReportResp]]:
    """Generate Report

     generate report for given type and filters

    Args:
        json_body (ModelGenerateReportReq):  Example: {'duration': 0, 'filters':
            {'include_dead_nodes': True, 'node_type': 'host', 'advanced_report_filters':
            {'image_name': ['image_name', 'image_name'], 'account_id': ['account_id', 'account_id'],
            'container_name': ['container_name', 'container_name'], 'scan_status': ['scan_status',
            'scan_status'], 'kubernetes_cluster_name': ['kubernetes_cluster_name',
            'kubernetes_cluster_name'], 'masked': [True, True], 'host_name': ['host_name',
            'host_name'], 'pod_name': ['pod_name', 'pod_name']}, 'scan_type': 'vulnerability',
            'scan_id': 'scan_id', 'severity_or_check_type': ['severity_or_check_type',
            'severity_or_check_type']}, 'report_type': 'pdf'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGenerateReportResp]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: ModelGenerateReportReq,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGenerateReportResp]]:
    """Generate Report

     generate report for given type and filters

    Args:
        json_body (ModelGenerateReportReq):  Example: {'duration': 0, 'filters':
            {'include_dead_nodes': True, 'node_type': 'host', 'advanced_report_filters':
            {'image_name': ['image_name', 'image_name'], 'account_id': ['account_id', 'account_id'],
            'container_name': ['container_name', 'container_name'], 'scan_status': ['scan_status',
            'scan_status'], 'kubernetes_cluster_name': ['kubernetes_cluster_name',
            'kubernetes_cluster_name'], 'masked': [True, True], 'host_name': ['host_name',
            'host_name'], 'pod_name': ['pod_name', 'pod_name']}, 'scan_type': 'vulnerability',
            'scan_id': 'scan_id', 'severity_or_check_type': ['severity_or_check_type',
            'severity_or_check_type']}, 'report_type': 'pdf'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGenerateReportResp]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ModelGenerateReportReq,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGenerateReportResp]]:
    """Generate Report

     generate report for given type and filters

    Args:
        json_body (ModelGenerateReportReq):  Example: {'duration': 0, 'filters':
            {'include_dead_nodes': True, 'node_type': 'host', 'advanced_report_filters':
            {'image_name': ['image_name', 'image_name'], 'account_id': ['account_id', 'account_id'],
            'container_name': ['container_name', 'container_name'], 'scan_status': ['scan_status',
            'scan_status'], 'kubernetes_cluster_name': ['kubernetes_cluster_name',
            'kubernetes_cluster_name'], 'masked': [True, True], 'host_name': ['host_name',
            'host_name'], 'pod_name': ['pod_name', 'pod_name']}, 'scan_type': 'vulnerability',
            'scan_id': 'scan_id', 'severity_or_check_type': ['severity_or_check_type',
            'severity_or_check_type']}, 'report_type': 'pdf'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGenerateReportResp]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: ModelGenerateReportReq,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGenerateReportResp]]:
    """Generate Report

     generate report for given type and filters

    Args:
        json_body (ModelGenerateReportReq):  Example: {'duration': 0, 'filters':
            {'include_dead_nodes': True, 'node_type': 'host', 'advanced_report_filters':
            {'image_name': ['image_name', 'image_name'], 'account_id': ['account_id', 'account_id'],
            'container_name': ['container_name', 'container_name'], 'scan_status': ['scan_status',
            'scan_status'], 'kubernetes_cluster_name': ['kubernetes_cluster_name',
            'kubernetes_cluster_name'], 'masked': [True, True], 'host_name': ['host_name',
            'host_name'], 'pod_name': ['pod_name', 'pod_name']}, 'scan_type': 'vulnerability',
            'scan_id': 'scan_id', 'severity_or_check_type': ['severity_or_check_type',
            'severity_or_check_type']}, 'report_type': 'pdf'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGenerateReportResp]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
