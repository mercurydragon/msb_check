from rest_framework import serializers

from app.models import Check


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check
        fields = ['tin', 'prsn', 'result', 'created']
