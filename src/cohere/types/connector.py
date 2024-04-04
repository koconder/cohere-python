# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import pydantic_v1
from ..core.unchecked_base_model import UncheckedBaseModel
from .connector_auth_status import ConnectorAuthStatus
from .connector_o_auth import ConnectorOAuth


class Connector(UncheckedBaseModel):
    """
    A connector allows you to integrate data sources with the '/chat' endpoint to create grounded generations with citations to the data source.
    documents to help answer users.
    """

    id: str = pydantic_v1.Field()
    """
    The unique identifier of the connector (used in both `/connectors` & `/chat` endpoints).
    This is automatically created from the name of the connector upon registration.
    """

    organization_id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The organization to which this connector belongs. This is automatically set to
    the organization of the user who created the connector.
    """

    name: str = pydantic_v1.Field()
    """
    A human-readable name for the connector.
    """

    description: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    A description of the connector.
    """

    url: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The URL of the connector that will be used to search for documents.
    """

    created_at: dt.datetime = pydantic_v1.Field()
    """
    The UTC time at which the connector was created.
    """

    updated_at: dt.datetime = pydantic_v1.Field()
    """
    The UTC time at which the connector was last updated.
    """

    excludes: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    A list of fields to exclude from the prompt (fields remain in the document).
    """

    auth_type: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The type of authentication/authorization used by the connector. Possible values: [oauth, service_auth]
    """

    oauth: typing.Optional[ConnectorOAuth] = pydantic_v1.Field(default=None)
    """
    The OAuth 2.0 configuration for the connector.
    """

    auth_status: typing.Optional[ConnectorAuthStatus] = pydantic_v1.Field(default=None)
    """
    The OAuth status for the user making the request. One of ["valid", "expired", ""]. Empty string (field is omitted) means the user has not authorized the connector yet.
    """

    active: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Whether the connector is active or not.
    """

    continue_on_failure: typing.Optional[bool] = pydantic_v1.Field(default=None)
    """
    Whether a chat request should continue or not if the request to this connector fails.
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
