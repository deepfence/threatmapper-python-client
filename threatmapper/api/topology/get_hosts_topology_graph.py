from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.graph_topology_filters import GraphTopologyFilters
from ...models.model_graph_result import ModelGraphResult
from ...types import Response


def _get_kwargs(
    *,
    body: GraphTopologyFilters,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/deepfence/graph/topology/hosts",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGraphResult]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ModelGraphResult.from_dict(response.json())

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
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGraphResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GraphTopologyFilters,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGraphResult]]:
    """Get Hosts Topology Graph

     Retrieve the full topology graph associated with the account from Hosts

    Args:
        body (GraphTopologyFilters):  Example: {'host_filter': ['host_filter', 'host_filter'],
            'field_filters': {'compare_filter': [{'greater_than': True, 'field_value': '',
            'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter':
            {'order_fields': [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0,
            'descending': True, 'field_name': 'field_name'}]}, 'contains_filter': {'filter_in':
            {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['', '']}},
            'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in':
            {'key': ['', '']}}}, 'container_filter': ['container_filter', 'container_filter'],
            'cloud_filter': ['cloud_filter', 'cloud_filter'], 'kubernetes_filter':
            ['kubernetes_filter', 'kubernetes_filter'], 'pod_filter': ['pod_filter', 'pod_filter'],
            'region_filter': ['region_filter', 'region_filter'], 'skip_connections': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGraphResult]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: GraphTopologyFilters,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGraphResult]]:
    """Get Hosts Topology Graph

     Retrieve the full topology graph associated with the account from Hosts

    Args:
        body (GraphTopologyFilters):  Example: {'host_filter': ['host_filter', 'host_filter'],
            'field_filters': {'compare_filter': [{'greater_than': True, 'field_value': '',
            'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter':
            {'order_fields': [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0,
            'descending': True, 'field_name': 'field_name'}]}, 'contains_filter': {'filter_in':
            {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['', '']}},
            'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in':
            {'key': ['', '']}}}, 'container_filter': ['container_filter', 'container_filter'],
            'cloud_filter': ['cloud_filter', 'cloud_filter'], 'kubernetes_filter':
            ['kubernetes_filter', 'kubernetes_filter'], 'pod_filter': ['pod_filter', 'pod_filter'],
            'region_filter': ['region_filter', 'region_filter'], 'skip_connections': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGraphResult]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GraphTopologyFilters,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGraphResult]]:
    """Get Hosts Topology Graph

     Retrieve the full topology graph associated with the account from Hosts

    Args:
        body (GraphTopologyFilters):  Example: {'host_filter': ['host_filter', 'host_filter'],
            'field_filters': {'compare_filter': [{'greater_than': True, 'field_value': '',
            'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter':
            {'order_fields': [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0,
            'descending': True, 'field_name': 'field_name'}]}, 'contains_filter': {'filter_in':
            {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['', '']}},
            'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in':
            {'key': ['', '']}}}, 'container_filter': ['container_filter', 'container_filter'],
            'cloud_filter': ['cloud_filter', 'cloud_filter'], 'kubernetes_filter':
            ['kubernetes_filter', 'kubernetes_filter'], 'pod_filter': ['pod_filter', 'pod_filter'],
            'region_filter': ['region_filter', 'region_filter'], 'skip_connections': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGraphResult]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GraphTopologyFilters,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGraphResult]]:
    """Get Hosts Topology Graph

     Retrieve the full topology graph associated with the account from Hosts

    Args:
        body (GraphTopologyFilters):  Example: {'host_filter': ['host_filter', 'host_filter'],
            'field_filters': {'compare_filter': [{'greater_than': True, 'field_value': '',
            'field_name': 'field_name'}, {'greater_than': True, 'field_value': '', 'field_name':
            'field_name'}], 'not_contains_filter': {'filter_in': {'key': ['', '']}}, 'order_filter':
            {'order_fields': [{'size': 0, 'descending': True, 'field_name': 'field_name'}, {'size': 0,
            'descending': True, 'field_name': 'field_name'}]}, 'contains_filter': {'filter_in':
            {'key': ['', '']}}, 'contains_in_array_filter': {'filter_in': {'key': ['', '']}},
            'match_filter': {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in':
            {'key': ['', '']}}}, 'container_filter': ['container_filter', 'container_filter'],
            'cloud_filter': ['cloud_filter', 'cloud_filter'], 'kubernetes_filter':
            ['kubernetes_filter', 'kubernetes_filter'], 'pod_filter': ['pod_filter', 'pod_filter'],
            'region_filter': ['region_filter', 'region_filter'], 'skip_connections': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, ModelGraphResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
