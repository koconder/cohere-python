# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import pydantic_v1
from .finetuned_model import FinetunedModel


class ListFinetunedModelsResponse(pydantic_v1.BaseModel):
    """
    Response to a request to list fine-tuned models.
    """

    finetuned_models: typing.Optional[typing.List[FinetunedModel]] = pydantic_v1.Field(default=None)
    """
    List of fine-tuned models matching the request.
    """

    next_page_token: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Pagination token to retrieve the next page of results. If the value is "",
    it means no further results for the request.
    """

    total_size: typing.Optional[int] = pydantic_v1.Field(default=None)
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
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
