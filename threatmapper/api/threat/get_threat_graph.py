from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.graph_threat_filters import GraphThreatFilters
from ...models.graph_threat_graph import GraphThreatGraph
from ...types import Response


def _get_kwargs(
    *,
    json_body: GraphThreatFilters,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/deepfence/graph/threat",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Optional[GraphThreatGraph]]]:
    if response.status_code == HTTPStatus.OK:
        _response_200 = response.json()
        response_200: Optional[GraphThreatGraph]
        if _response_200 is None:
            response_200 = None
        else:
            response_200 = GraphThreatGraph.from_dict(_response_200)

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
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Optional[GraphThreatGraph]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: GraphThreatFilters,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Optional[GraphThreatGraph]]]:
    """Get Threat Graph

     Retrieve the full threat graph associated with the account

    Args:
        json_body (GraphThreatFilters):  Example: {'cloud_resource_only': True, 'aws_filter':
            {'account_ids': ['account_ids', 'account_ids']}, 'gcp_filter': {'account_ids':
            ['account_ids', 'account_ids']}, 'type': 'all', 'azure_filter': {'account_ids':
            ['account_ids', 'account_ids']}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Optional[GraphThreatGraph]]]
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
    json_body: GraphThreatFilters,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Optional[GraphThreatGraph]]]:
    """Get Threat Graph

     Retrieve the full threat graph associated with the account

    Args:
        json_body (GraphThreatFilters):  Example: {'cloud_resource_only': True, 'aws_filter':
            {'account_ids': ['account_ids', 'account_ids']}, 'gcp_filter': {'account_ids':
            ['account_ids', 'account_ids']}, 'type': 'all', 'azure_filter': {'account_ids':
            ['account_ids', 'account_ids']}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Optional[GraphThreatGraph]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: GraphThreatFilters,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Optional[GraphThreatGraph]]]:
    """Get Threat Graph

     Retrieve the full threat graph associated with the account

    Args:
        json_body (GraphThreatFilters):  Example: {'cloud_resource_only': True, 'aws_filter':
            {'account_ids': ['account_ids', 'account_ids']}, 'gcp_filter': {'account_ids':
            ['account_ids', 'account_ids']}, 'type': 'all', 'azure_filter': {'account_ids':
            ['account_ids', 'account_ids']}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Optional[GraphThreatGraph]]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: GraphThreatFilters,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Optional[GraphThreatGraph]]]:
    """Get Threat Graph

     Retrieve the full threat graph associated with the account

    Args:
        json_body (GraphThreatFilters):  Example: {'cloud_resource_only': True, 'aws_filter':
            {'account_ids': ['account_ids', 'account_ids']}, 'gcp_filter': {'account_ids':
            ['account_ids', 'account_ids']}, 'type': 'all', 'azure_filter': {'account_ids':
            ['account_ids', 'account_ids']}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Optional[GraphThreatGraph]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
