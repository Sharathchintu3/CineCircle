from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    class Meta:
        model = Review

        fields = [
            "id",
            "movie",
            "username",
            "rating",
            "title",
            "content",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "username",
            "created_at",
            "updated_at",
        ]
    def validate_rating(self,value):
        if value < 0.5 or value >5:
            raise serializers.ValidationError(
                "rating must be between 0.5 and 5."
            )
        return value

    def validate(self, attrs):
        user = self.context["request"].user
        movie = attrs["movie"]
        queryset = Review.objects.filter(user=user, movie=movie)

        if self.instance:
            queryset = queryset.exclude(pk = self.instance.pk)
        if queryset.exists():
            raise serializers.ValidationError(
                "You have already reviewed this Movie"
            )
        return attrs