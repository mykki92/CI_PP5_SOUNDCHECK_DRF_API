from django.db import IntegrityError
from rest_framework import serializers
from likes.models import Check


class CheckSerializer(serializers.ModelSerializer):
    """
    A class for the like serializer.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Check
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        """
        A function to handle duplicate likes
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
