from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_docs_bad_request_response import ApiDocsBadRequestResponse
from ...models.api_docs_failure_response import ApiDocsFailureResponse
from ...models.model_secret_rule import ModelSecretRule
from ...models.search_search_node_req import SearchSearchNodeReq
from ...types import Response


def _get_kwargs(
    *,
    body: SearchSearchNodeReq,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/deepfence/search/secret-rules",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelSecretRule"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ModelSecretRule.from_dict(response_200_item_data)

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
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelSecretRule"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchSearchNodeReq,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelSecretRule"]]]:
    """Search Secret Rules

     Search across all the data associated with secret rules

    Args:
        body (SearchSearchNodeReq):  Example: {'node_filter': {'in_field_filter':
            ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter': [{'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True,
            'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in':
            {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True,
            'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'extended_node_filter': {'in_field_filter':
            ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter': [{'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True,
            'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in':
            {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True,
            'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'related_node_filter': {'node_filter':
            {'in_field_filter': ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter':
            [{'greater_than': True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter':
            {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0,
            'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True,
            'field_name': 'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'next_filter': None, 'relation_ship':
            'relation_ship'}, 'window': {'offset': 0, 'size': 6}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['ModelSecretRule']]]
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
    body: SearchSearchNodeReq,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelSecretRule"]]]:
    """Search Secret Rules

     Search across all the data associated with secret rules

    Args:
        body (SearchSearchNodeReq):  Example: {'node_filter': {'in_field_filter':
            ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter': [{'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True,
            'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in':
            {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True,
            'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'extended_node_filter': {'in_field_filter':
            ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter': [{'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True,
            'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in':
            {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True,
            'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'related_node_filter': {'node_filter':
            {'in_field_filter': ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter':
            [{'greater_than': True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter':
            {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0,
            'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True,
            'field_name': 'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'next_filter': None, 'relation_ship':
            'relation_ship'}, 'window': {'offset': 0, 'size': 6}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['ModelSecretRule']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchSearchNodeReq,
) -> Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelSecretRule"]]]:
    """Search Secret Rules

     Search across all the data associated with secret rules

    Args:
        body (SearchSearchNodeReq):  Example: {'node_filter': {'in_field_filter':
            ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter': [{'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True,
            'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in':
            {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True,
            'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'extended_node_filter': {'in_field_filter':
            ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter': [{'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True,
            'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in':
            {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True,
            'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'related_node_filter': {'node_filter':
            {'in_field_filter': ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter':
            [{'greater_than': True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter':
            {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0,
            'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True,
            'field_name': 'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'next_filter': None, 'relation_ship':
            'relation_ship'}, 'window': {'offset': 0, 'size': 6}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['ModelSecretRule']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SearchSearchNodeReq,
) -> Optional[Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List["ModelSecretRule"]]]:
    """Search Secret Rules

     Search across all the data associated with secret rules

    Args:
        body (SearchSearchNodeReq):  Example: {'node_filter': {'in_field_filter':
            ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter': [{'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True,
            'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in':
            {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True,
            'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'extended_node_filter': {'in_field_filter':
            ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter': [{'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than': True,
            'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter': {'filter_in':
            {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0, 'descending': True,
            'field_name': 'field_name'}, {'size': 0, 'descending': True, 'field_name':
            'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'related_node_filter': {'node_filter':
            {'in_field_filter': ['in_field_filter', 'in_field_filter'], 'filters': {'compare_filter':
            [{'greater_than': True, 'field_value': '', 'field_name': 'field_name'}, {'greater_than':
            True, 'field_value': '', 'field_name': 'field_name'}], 'not_contains_filter':
            {'filter_in': {'key': ['', '']}}, 'order_filter': {'order_fields': [{'size': 0,
            'descending': True, 'field_name': 'field_name'}, {'size': 0, 'descending': True,
            'field_name': 'field_name'}]}, 'contains_filter': {'filter_in': {'key': ['', '']}},
            'contains_in_array_filter': {'filter_in': {'key': ['', '']}}, 'match_filter':
            {'filter_in': {'key': ['', '']}}, 'match_in_array_filter': {'filter_in': {'key': ['',
            '']}}}, 'window': {'offset': 0, 'size': 6}}, 'next_filter': None, 'relation_ship':
            'relation_ship'}, 'window': {'offset': 0, 'size': 6}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiDocsBadRequestResponse, ApiDocsFailureResponse, List['ModelSecretRule']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
