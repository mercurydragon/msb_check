from datetime import datetime
from unittest.mock import patch

import pytest

from app.models import Check
from app.serializers import CheckSerializer


@pytest.mark.parametrize(
    'value, expected',
    (
        ({'tin': 123}, True),
        ({'prsn': 456}, True),
        ({'tin': 123, 'prsn': 456}, False),
        ({}, False),
        ({'tin': 'qwerty'}, False),
        ({'prsn': 'qwerty'}, False),
        ({'tin':  12345678901234567890}, False),
        ({'prsn': 12345678901234567890}, False),
    ),
)
def test_validate_serializer(value, expected):
    serializer = CheckSerializer(data=value)
    assert serializer.is_valid() == expected


@pytest.mark.django_db
def test_not_created_existed_check():
    check = Check.objects.create(tin='123', result=True)
    serializer = CheckSerializer(data={'tin': '123'})
    with patch('app.helpers.MSBAPIHelper.is_msb') as is_msb:
        assert serializer.create({'tin': '123'}) == check
        is_msb.assert_not_called()
        assert Check.objects.all().count() == 1


@pytest.mark.django_db
def test_not_use_too_old_check():
    check = Check.objects.create(tin='123', result=True, created=datetime(2019, 1, 1))
    serializer = CheckSerializer(data={'tin': '123'})
    with patch('app.helpers.MSBAPIHelper.is_msb', return_value=False) as is_msb:
        assert serializer.create({'tin': '123'}) != check
        is_msb.assert_called_once_with({'tin': '123', 'result': False})

