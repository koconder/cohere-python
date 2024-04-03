# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

import pydantic

IS_PYDANTIC_V2 = pydantic.VERSION.startswith("2.")

if IS_PYDANTIC_V2:
    import pydantic.v1 as pydantic_v1  # type: ignore
else:
    import pydantic  as pydantic_v1  # type: ignore


class EmbedByTypeResponseEmbeddings(pydantic.BaseModel):
    """
    An object with different embedding types. The length of each embedding type array will be the same as the length of the original `texts` array.
    """

    float_: typing.Optional[typing.List[typing.List[float]]] = pydantic.Field(alias="float", default=None)
    """
    An array of float embeddings.
    """

    int8: typing.Optional[typing.List[typing.List[float]]] = pydantic.Field(default=None)
    """
    An array of signed int8 embeddings. Each value is between -128 and 127.
    """

    uint8: typing.Optional[typing.List[typing.List[float]]] = pydantic.Field(default=None)
    """
    An array of unsigned int8 embeddings. Each value is between 0 and 255.
    """

    binary: typing.Optional[typing.List[typing.List[float]]] = pydantic.Field(default=None)
    """
    An array of packed signed binary embeddings. The length of each binary embedding is 1/8 the length of the float embeddings of the provided model. Each value is between -128 and 127.
    """

    ubinary: typing.Optional[typing.List[typing.List[float]]] = pydantic.Field(default=None)
    """
    An array of packed unsigned binary embeddings. The length of each binary embedding is 1/8 the length of the float embeddings of the provided model. Each value is between 0 and 255.
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
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
