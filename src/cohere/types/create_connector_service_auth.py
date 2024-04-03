# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .auth_token_type import AuthTokenType

import pydantic

IS_PYDANTIC_V2 = pydantic.VERSION.startswith("2.")

if IS_PYDANTIC_V2:
    import pydantic.v1 as pydantic_v1  # type: ignore
else:
    import pydantic  as pydantic_v1  # type: ignore


class CreateConnectorServiceAuth(pydantic.BaseModel):
    type: AuthTokenType
    token: str = pydantic.Field()
    """
    The token that will be used in the HTTP Authorization header when making requests to the connector. This field is encrypted at rest and never returned in a response.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
