
from django.db.models import Count, Avg
from rest_framework import serializers
from .models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = [
            "id",
            "tmdb_id",
            "name",

        ]



class MovieSerializer(serializers.ModelSerializer):

    average_rating = serializers.FloatField(read_only=True)
    total_reviews = serializers.IntegerField(read_only=True)
    rating_summary = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            "id",
            "tmdb_id",
            "title",
            "overview",
            "poster_path",
            "backdrop_path",
            "release_date",
            "runtime",
            "original_language",
            "popularity",
            "vote_average",
            "vote_count",
            "genres",
            "average_rating",
            "total_reviews",
            "rating_summary",
        ]

    def get_rating_summary(self, obj):
        from reviews.models import Review
        summary = {
            "5":0,
            "4.5":0,
            "4":0,
            "3.5": 0,
            "3": 0,
            "2.5": 0,
            "2": 0,
            "1.5": 0,
            "1": 0,
            "0":0,
        }
        ratings = (
            Review.objects.filter(movie=obj)
            .values("rating")
            .annotate(count=Count("id"))
        )

        for item in ratings:
            summary[str(item["rating"])] = item["count"]

        return summary