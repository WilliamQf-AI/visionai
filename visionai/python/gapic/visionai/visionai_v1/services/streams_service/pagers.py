# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from typing import Any, AsyncIterator, Awaitable, Callable, Sequence, Tuple, Optional, Iterator

from visionai.python.gapic.visionai.visionai_v1.types import common
from visionai.python.gapic.visionai.visionai_v1.types import streams_resources
from visionai.python.gapic.visionai.visionai_v1.types import streams_service


class ListClustersPager:
    """A pager for iterating through ``list_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListClustersResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``clusters`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListClusters`` requests and continue to iterate
    through the ``clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., streams_service.ListClustersResponse],
            request: streams_service.ListClustersRequest,
            response: streams_service.ListClustersResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListClustersRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListClustersResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = streams_service.ListClustersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[streams_service.ListClustersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[common.Cluster]:
        for page in self.pages:
            yield from page.clusters

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListClustersAsyncPager:
    """A pager for iterating through ``list_clusters`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListClustersResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``clusters`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListClusters`` requests and continue to iterate
    through the ``clusters`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListClustersResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[streams_service.ListClustersResponse]],
            request: streams_service.ListClustersRequest,
            response: streams_service.ListClustersResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListClustersRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListClustersResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = streams_service.ListClustersRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[streams_service.ListClustersResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[common.Cluster]:
        async def async_generator():
            async for page in self.pages:
                for response in page.clusters:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListStreamsPager:
    """A pager for iterating through ``list_streams`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListStreamsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``streams`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListStreams`` requests and continue to iterate
    through the ``streams`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., streams_service.ListStreamsResponse],
            request: streams_service.ListStreamsRequest,
            response: streams_service.ListStreamsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListStreamsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListStreamsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = streams_service.ListStreamsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[streams_service.ListStreamsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[streams_resources.Stream]:
        for page in self.pages:
            yield from page.streams

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListStreamsAsyncPager:
    """A pager for iterating through ``list_streams`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListStreamsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``streams`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListStreams`` requests and continue to iterate
    through the ``streams`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListStreamsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[streams_service.ListStreamsResponse]],
            request: streams_service.ListStreamsRequest,
            response: streams_service.ListStreamsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListStreamsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListStreamsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = streams_service.ListStreamsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[streams_service.ListStreamsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[streams_resources.Stream]:
        async def async_generator():
            async for page in self.pages:
                for response in page.streams:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListEventsPager:
    """A pager for iterating through ``list_events`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListEventsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``events`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListEvents`` requests and continue to iterate
    through the ``events`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., streams_service.ListEventsResponse],
            request: streams_service.ListEventsRequest,
            response: streams_service.ListEventsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListEventsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListEventsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = streams_service.ListEventsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[streams_service.ListEventsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[streams_resources.Event]:
        for page in self.pages:
            yield from page.events

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListEventsAsyncPager:
    """A pager for iterating through ``list_events`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListEventsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``events`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListEvents`` requests and continue to iterate
    through the ``events`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListEventsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[streams_service.ListEventsResponse]],
            request: streams_service.ListEventsRequest,
            response: streams_service.ListEventsResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListEventsRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListEventsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = streams_service.ListEventsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[streams_service.ListEventsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[streams_resources.Event]:
        async def async_generator():
            async for page in self.pages:
                for response in page.events:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListSeriesPager:
    """A pager for iterating through ``list_series`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListSeriesResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``series`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListSeries`` requests and continue to iterate
    through the ``series`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListSeriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., streams_service.ListSeriesResponse],
            request: streams_service.ListSeriesRequest,
            response: streams_service.ListSeriesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListSeriesRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListSeriesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = streams_service.ListSeriesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterator[streams_service.ListSeriesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterator[streams_resources.Series]:
        for page in self.pages:
            yield from page.series

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class ListSeriesAsyncPager:
    """A pager for iterating through ``list_series`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.visionai_v1.types.ListSeriesResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``series`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListSeries`` requests and continue to iterate
    through the ``series`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.visionai_v1.types.ListSeriesResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[..., Awaitable[streams_service.ListSeriesResponse]],
            request: streams_service.ListSeriesRequest,
            response: streams_service.ListSeriesResponse,
            *,
            metadata: Sequence[Tuple[str, str]] = ()):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.visionai_v1.types.ListSeriesRequest):
                The initial request object.
            response (google.cloud.visionai_v1.types.ListSeriesResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = streams_service.ListSeriesRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterator[streams_service.ListSeriesResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response
    def __aiter__(self) -> AsyncIterator[streams_resources.Series]:
        async def async_generator():
            async for page in self.pages:
                for response in page.series:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
