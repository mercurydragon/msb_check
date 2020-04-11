import re
from datetime import timedelta

from django.utils.timezone import now
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField

from app.helpers import MSBAPIHelper
from app.models import Check


def only_digits_validator(value):
    if re.search(r'\D', value, re.U):
        raise ValidationError('Field should contain only digits')


class CheckSerializer(serializers.ModelSerializer):
    tin = CharField(
        max_length=12,
        required=False,
        validators=[only_digits_validator]
    )
    prsn = CharField(
        max_length=15,
        required=False,
        validators=[only_digits_validator]
    )

    class Meta:
        model = Check
        fields = ['tin', 'prsn', 'result', 'created']

    def validate(self, data):
        """
        Check that tin or person is passed neither both together or no one
        """
        conditions = (data.get('tin') is not None, data.get('prsn') is not None)
        if not all(conditions) and any(conditions):
            return data

        raise serializers.ValidationError('You should pass tin or prsn')

    def create(self, validated_data):
        data = validated_data.copy()
        relevant_check = Check.objects.filter(**data, created__gte=(now() - timedelta(minutes=5))).first()
        if relevant_check:
            return relevant_check
        data['result'] = MSBAPIHelper().is_msb(data)
        return super().create(data)


