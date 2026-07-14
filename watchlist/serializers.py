from rest_framework import serializers
from .models import Watchlist

class WatchlistSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    tmdb_id = serializers.IntegerField(source="movie.tmdb_id", read_only=True)

    class Meta:
        model = Watchlist

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

        if Watchlist.objects.filter(user=user, movie=movie).exists():
            raise serializers.ValidationError(
                "Movie is already in the watchlist."
            )
        return attrs