from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.graph_threat_filters import GraphThreatFilters
from ...models.graph_threat_graph_type_0 import GraphThreatGraphType0
from ...types import Response


def _get_kwargs(
    *,
    body: GraphThreatFilters,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/deepfence/graph/threat",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Union["GraphThreatGraphType0", None]]]:
    if response.status_code == HTTPStatus.OK:

        def _parse_response_200(data: object) -> Union["GraphThreatGraphType0", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_graph_threat_graph_type_0 = GraphThreatGraphType0.from_dict(data)

                return componentsschemas_graph_threat_graph_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GraphThreatGraphType0", None], data)

        response_200 = _parse_response_200(response.json())

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
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Union["GraphThreatGraphType0", None]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: GraphThreatFilters,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Union["GraphThreatGraphType0", None]]]:
    """Get Threat Graph

     Retrieve the full threat graph associated with the account

    Args:
        body (GraphThreatFilters):  Example: {'cloud_resource_only': True, 'aws_filter':
            {'account_ids': ['account_ids', 'account_ids']}, 'gcp_filter': {'account_ids':
            ['account_ids', 'account_ids']}, 'type': 'all', 'azure_filter': {'account_ids':
            ['account_ids', 'account_ids']}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Union['GraphThreatGraphType0', None]]]
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
    body: GraphThreatFilters,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Union["GraphThreatGraphType0", None]]]:
    """Get Threat Graph

     Retrieve the full threat graph associated with the account

    Args:
        body (GraphThreatFilters):  Example: {'cloud_resource_only': True, 'aws_filter':
            {'account_ids': ['account_ids', 'account_ids']}, 'gcp_filter': {'account_ids':
            ['account_ids', 'account_ids']}, 'type': 'all', 'azure_filter': {'account_ids':
            ['account_ids', 'account_ids']}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Union['GraphThreatGraphType0', None]]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: GraphThreatFilters,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Union["GraphThreatGraphType0", None]]]:
    """Get Threat Graph

     Retrieve the full threat graph associated with the account

    Args:
        body (GraphThreatFilters):  Example: {'cloud_resource_only': True, 'aws_filter':
            {'account_ids': ['account_ids', 'account_ids']}, 'gcp_filter': {'account_ids':
            ['account_ids', 'account_ids']}, 'type': 'all', 'azure_filter': {'account_ids':
            ['account_ids', 'account_ids']}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Union['GraphThreatGraphType0', None]]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: GraphThreatFilters,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Union["GraphThreatGraphType0", None]]]:
    """Get Threat Graph

     Retrieve the full threat graph associated with the account

    Args:
        body (GraphThreatFilters):  Example: {'cloud_resource_only': True, 'aws_filter':
            {'account_ids': ['account_ids', 'account_ids']}, 'gcp_filter': {'account_ids':
            ['account_ids', 'account_ids']}, 'type': 'all', 'azure_filter': {'account_ids':
            ['account_ids', 'account_ids']}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, Union['GraphThreatGraphType0', None]]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
