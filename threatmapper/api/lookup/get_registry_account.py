from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.lookup_lookup_filter import LookupLookupFilter
from ...models.model_registry_account import ModelRegistryAccount
from ...types import Response


def _get_kwargs(
    *,
    body: LookupLookupFilter,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/deepfence/lookup/registryaccount",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelRegistryAccount"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelRegistryAccount.from_dict(response_200_item_data)

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
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelRegistryAccount"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: LookupLookupFilter,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelRegistryAccount"]]]:
    """Get Images in Registry

     List all the images present in the given registry

    Args:
        body (LookupLookupFilter):  Example: {'in_field_filter': ['in_field_filter',
            'in_field_filter'], 'window': {'offset': 0, 'size': 6}, 'node_ids': ['node_ids',
            'node_ids']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['ModelRegistryAccount']]]
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
    body: LookupLookupFilter,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelRegistryAccount"]]]:
    """Get Images in Registry

     List all the images present in the given registry

    Args:
        body (LookupLookupFilter):  Example: {'in_field_filter': ['in_field_filter',
            'in_field_filter'], 'window': {'offset': 0, 'size': 6}, 'node_ids': ['node_ids',
            'node_ids']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['ModelRegistryAccount']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: LookupLookupFilter,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelRegistryAccount"]]]:
    """Get Images in Registry

     List all the images present in the given registry

    Args:
        body (LookupLookupFilter):  Example: {'in_field_filter': ['in_field_filter',
            'in_field_filter'], 'window': {'offset': 0, 'size': 6}, 'node_ids': ['node_ids',
            'node_ids']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['ModelRegistryAccount']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: LookupLookupFilter,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelRegistryAccount"]]]:
    """Get Images in Registry

     List all the images present in the given registry

    Args:
        body (LookupLookupFilter):  Example: {'in_field_filter': ['in_field_filter',
            'in_field_filter'], 'window': {'offset': 0, 'size': 6}, 'node_ids': ['node_ids',
            'node_ids']}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['ModelRegistryAccount']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
