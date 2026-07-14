from rest_framework import serializers
from .models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    tmdb_id = serializers.IntegerField(source="movie.tmdb_id", read_only=True)

    class Meta:
        model = Favorite

        fields = [
            "id",
            "tmdb_id",
            "movie_title",
            "added_at",
            "movie",
        ]

        read_only_fields = [
            "id",
            "movie_title",
            "tmdb_id",
            "added_at",
        ]

    def validate(self, attrs):
        user = self.context["request"].user
        movie = attrs["movie"]

        if Favorite.objects.filter(user=user, movie=movie).exists():
            raise serializers.ValidationError(
                "Movie is already in the favorites."
            )
        return attrs