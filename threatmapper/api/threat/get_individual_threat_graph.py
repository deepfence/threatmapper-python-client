from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.graph_individual_threat_graph import GraphIndividualThreatGraph
from ...models.graph_individual_threat_graph_request import GraphIndividualThreatGraphRequest
from ...types import Response


def _get_kwargs(
    *,
    json_body: GraphIndividualThreatGraphRequest,
) -> Dict[str, Any]:
    pass

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/deepfence/graph/threat/individual",
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["GraphIndividualThreatGraph"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GraphIndividualThreatGraph.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["GraphIndividualThreatGraph"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: GraphIndividualThreatGraphRequest,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["GraphIndividualThreatGraph"]]]:
    """Get Vulnerability Threat Graph

     Retrieve threat graph associated with vulnerabilities

    Args:
        json_body (GraphIndividualThreatGraphRequest):  Example: {'graph_type':
            'most_vulnerable_attack_paths', 'issue_type': 'vulnerability', 'node_ids': ['node_ids',
            'node_ids']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['GraphIndividualThreatGraph']]]
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
    json_body: GraphIndividualThreatGraphRequest,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["GraphIndividualThreatGraph"]]]:
    """Get Vulnerability Threat Graph

     Retrieve threat graph associated with vulnerabilities

    Args:
        json_body (GraphIndividualThreatGraphRequest):  Example: {'graph_type':
            'most_vulnerable_attack_paths', 'issue_type': 'vulnerability', 'node_ids': ['node_ids',
            'node_ids']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['GraphIndividualThreatGraph']]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: GraphIndividualThreatGraphRequest,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["GraphIndividualThreatGraph"]]]:
    """Get Vulnerability Threat Graph

     Retrieve threat graph associated with vulnerabilities

    Args:
        json_body (GraphIndividualThreatGraphRequest):  Example: {'graph_type':
            'most_vulnerable_attack_paths', 'issue_type': 'vulnerability', 'node_ids': ['node_ids',
            'node_ids']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['GraphIndividualThreatGraph']]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: GraphIndividualThreatGraphRequest,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["GraphIndividualThreatGraph"]]]:
    """Get Vulnerability Threat Graph

     Retrieve threat graph associated with vulnerabilities

    Args:
        json_body (GraphIndividualThreatGraphRequest):  Example: {'graph_type':
            'most_vulnerable_attack_paths', 'issue_type': 'vulnerability', 'node_ids': ['node_ids',
            'node_ids']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['GraphIndividualThreatGraph']]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
