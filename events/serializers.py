from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Events model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url'
    )
    comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        """
        A function to validate image data size, height and width
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image size must not exceed 2MB!'
                )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height must not exceed 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width must not exceed 4096px!'
            )
        return value

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'is_owner', 'created_at', 'updated_at', 'title',
            'description', 'image', 'image_filter', 'event_start', 'event_end', 
            'location', 'comments_count', 'profile_id', 'profile_image',
        ]
