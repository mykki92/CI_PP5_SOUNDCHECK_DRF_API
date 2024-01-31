from rest_framework import serializers
from .models import Event
from interested.models import Interested
from attending.models import Attending


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
    interested_count = serializers.ReadOnlyField()
    attending_count = serializers.ReadOnlyField()
    interested_id = serializers.SerializerMethodField()
    attending_id = serializers.SerializerMethodField()

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

    def get_interested_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            interested = Interested.objects.filter(
                owner=user, event=obj
            ).first()
            return interested.id if interested else None
        return None

    def get_attending_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            attending = Attending.objects.filter(
                owner=user, event=obj
            ).first()
            return attending.id if attending else None
        return None

    class Meta:
        model = Event
        fields = [
            'id', 'owner', 'is_owner', 'created_at', 'updated_at', 'title',
            'description', 'image', 'image_filter', 'event_start', 'event_end', 
            'location', 'comments_count', 'interested_count', 'interested_id',
            'attending_count', 'attending_id', 'profile_id', 'profile_image',
        ]
