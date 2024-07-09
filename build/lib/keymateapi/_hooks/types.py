"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from abc import ABC, abstractmethod
from typing import Any, Callable, List, Optional, Tuple, Union


class HookContext:
    operation_id: str
    oauth2_scopes: Optional[List[str]] = None
    security_source: Optional[Union[Any, Callable[[], Any]]] = None

    def __init__(self, operation_id: str, oauth2_scopes: Optional[List[str]], security_source: Optional[Union[Any, Callable[[], Any]]]):
        self.operation_id = operation_id
        self.oauth2_scopes = oauth2_scopes
        self.security_source = security_source


class BeforeRequestContext(HookContext):
    def __init__(self, hook_ctx: HookContext):
        super().__init__(hook_ctx.operation_id, hook_ctx.oauth2_scopes, hook_ctx.security_source)


class AfterSuccessContext(HookContext):
    def __init__(self, hook_ctx: HookContext):
        super().__init__(hook_ctx.operation_id, hook_ctx.oauth2_scopes, hook_ctx.security_source)
    


class AfterErrorContext(HookContext):
    def __init__(self, hook_ctx: HookContext):
        super().__init__(hook_ctx.operation_id, hook_ctx.oauth2_scopes, hook_ctx.security_source)


class SDKInitHook(ABC):
    @abstractmethod
    def sdk_init(self, base_url: str, client: requests_http.Session) -> Tuple[str, requests_http.Session]:
        pass


class BeforeRequestHook(ABC):
    @abstractmethod
    def before_request(self, hook_ctx: BeforeRequestContext, request: requests_http.PreparedRequest) -> Union[requests_http.PreparedRequest, Exception]:
        pass


class AfterSuccessHook(ABC):
    @abstractmethod
    def after_success(self, hook_ctx: AfterSuccessContext, response: requests_http.Response) -> Union[requests_http.Response, Exception]:
        pass


class AfterErrorHook(ABC):
    @abstractmethod
    def after_error(self, hook_ctx: AfterErrorContext, response: Optional[requests_http.Response], error: Optional[Exception]) -> Union[Tuple[Optional[requests_http.Response], Optional[Exception]], Exception]:
        pass


class Hooks(ABC):
    @abstractmethod
    def register_sdk_init_hook(self, hook: SDKInitHook):
        pass

    @abstractmethod
    def register_before_request_hook(self, hook: BeforeRequestHook):
        pass

    @abstractmethod
    def register_after_success_hook(self, hook: AfterSuccessHook):
        pass

    @abstractmethod
    def register_after_error_hook(self, hook: AfterErrorHook):
        pass
