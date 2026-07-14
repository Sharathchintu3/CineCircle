from rest_framework import serializers
from .models import Follow

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = [
            "id",
            "following",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]

    def validate(self, attrs):
        user = self.context["request"].user
        following = attrs["following"]

        if user == following:
            raise serializers.ValidationError(
                "You cannot follow yourself."
            )

        if Follow.objects.filter(follower=user, following=following).exists():
            raise serializers.ValidationError(
                "You're already following this user."
            )
        return attrs