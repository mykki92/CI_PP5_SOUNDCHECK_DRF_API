from rest_framework import serializers
from django.db import IntegrityError

from .models import Interested


class InterestedSerializer(serializers.ModelSerializer):
    """
    Serializer for the Interested model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Interested
        fields = [
            'id', 'owner', 'created_at', 'event',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'You are already interested in this event!'
            })
            