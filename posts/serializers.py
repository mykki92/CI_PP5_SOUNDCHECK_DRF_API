from rest_framework import serializers
from posts.models import Post
from likes.models import Check


class PostSerializer(serializers.ModelSerializer):
    """
    A class for the PostSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    check_id = serializers.SerializerMethodField()
    check_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

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

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_check_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            check = Check.objects.filter(
                owner=user, post=obj
            ).first()
            return check.id if check else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'check_id',
            'check_count', 'comments_count',
        ]
