# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .event import Event

import pydantic

IS_PYDANTIC_V2 = pydantic.VERSION.startswith("2.")

if IS_PYDANTIC_V2:
    import pydantic.v1 as pydantic_v1  # type: ignore
else:
    import pydantic  as pydantic_v1  # type: ignore


class ListEventsResponse(pydantic.BaseModel):
    """
    Response to a request to list events of a fine-tuned model.
    """

    events: typing.Optional[typing.List[Event]] = pydantic.Field(default=None)
    """
    List of events for the fine-tuned model.
    """

    next_page_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Pagination token to retrieve the next page of results. If the value is "",
    it means no further results for the request.
    """

    total_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total count of results.
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
