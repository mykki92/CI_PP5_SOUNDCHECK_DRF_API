from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    A class for the PostSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        """
        A function to validate image data size, height and width
        """
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size must not exceed 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height must not exceed 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width muss not exceed 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image'
        ]