from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.list_generative_ai_integration_integration_type import ListGenerativeAiIntegrationIntegrationType
from ...models.model_generative_ai_integration_list_response import ModelGenerativeAiIntegrationListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    integration_type: Union[Unset, None, ListGenerativeAiIntegrationIntegrationType] = UNSET,
) -> Dict[str, Any]:
    pass

    params: Dict[str, Any] = {}
    json_integration_type: Union[Unset, None, str] = UNSET
    if not isinstance(integration_type, Unset):
        json_integration_type = integration_type.value if integration_type else None

    params["integration_type"] = json_integration_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/deepfence/generative-ai-integration",
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelGenerativeAiIntegrationListResponse"]]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelGenerativeAiIntegrationListResponse.from_dict(response_200_item_data)

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
) -> Response[
    Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelGenerativeAiIntegrationListResponse"]]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    integration_type: Union[Unset, None, ListGenerativeAiIntegrationIntegrationType] = UNSET,
) -> Response[
    Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelGenerativeAiIntegrationListResponse"]]
]:
    """List Generative AI Integrations

     List all the added Generative AI Integrations

    Args:
        integration_type (Union[Unset, None, ListGenerativeAiIntegrationIntegrationType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['ModelGenerativeAiIntegrationListResponse']]]
    """

    kwargs = _get_kwargs(
        integration_type=integration_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    integration_type: Union[Unset, None, ListGenerativeAiIntegrationIntegrationType] = UNSET,
) -> Optional[
    Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelGenerativeAiIntegrationListResponse"]]
]:
    """List Generative AI Integrations

     List all the added Generative AI Integrations

    Args:
        integration_type (Union[Unset, None, ListGenerativeAiIntegrationIntegrationType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['ModelGenerativeAiIntegrationListResponse']]
    """

    return sync_detailed(
        client=client,
        integration_type=integration_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    integration_type: Union[Unset, None, ListGenerativeAiIntegrationIntegrationType] = UNSET,
) -> Response[
    Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelGenerativeAiIntegrationListResponse"]]
]:
    """List Generative AI Integrations

     List all the added Generative AI Integrations

    Args:
        integration_type (Union[Unset, None, ListGenerativeAiIntegrationIntegrationType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['ModelGenerativeAiIntegrationListResponse']]]
    """

    kwargs = _get_kwargs(
        integration_type=integration_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    integration_type: Union[Unset, None, ListGenerativeAiIntegrationIntegrationType] = UNSET,
) -> Optional[
    Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelGenerativeAiIntegrationListResponse"]]
]:
    """List Generative AI Integrations

     List all the added Generative AI Integrations

    Args:
        integration_type (Union[Unset, None, ListGenerativeAiIntegrationIntegrationType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['ModelGenerativeAiIntegrationListResponse']]
    """

    return (
        await asyncio_detailed(
            client=client,
            integration_type=integration_type,
        )
    ).parsed
