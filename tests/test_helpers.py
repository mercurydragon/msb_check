import requests_mock
import pytest
from django.conf import settings

from app.helpers import MSBAPIHelper
from tests.conftest import IS_MSB_API_RESPONSE, NOT_MSB_API_RESPONSE


@pytest.mark.parametrize(
    'response, status, expected',
    (
        (IS_MSB_API_RESPONSE, 200, True),
        (NOT_MSB_API_RESPONSE, 200, False),
        ({}, 400, None),
    ),
)
def test_is_msb(response, status, expected):
    assert False
    with requests_mock.Mocker() as mock_request:
        mock_request.post(settings.EXTERNAL_API_URL, json=response, status_code=status)
        assert MSBAPIHelper().is_msb({'tin': 123}) == expected


@pytest.mark.parametrize(
    'value, expected',
    (
        ({'tin': 123}, 123),
        ({'prsn': 456}, 456),
    ),
)
def test_prepare_params(value, expected):
    assert MSBAPIHelper().prepare_params(value) == {'query': expected}


@pytest.mark.parametrize(
    'value',
    (
        ({'tin': 123, 'prsn': 456}),
        ({}),
    ),
)
def test_prepare_params_error(value):
    with pytest.raises(AssertionError):
        assert MSBAPIHelper().prepare_params(value)

