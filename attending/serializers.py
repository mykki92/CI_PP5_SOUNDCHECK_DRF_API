from rest_framework import serializers
from django.db import IntegrityError

from .models import Attending


class AttendingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Attending model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Attending
        fields = [
            'id', 'owner', 'created_at', 'event',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You are already attending this event!'
            })
