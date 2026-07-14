from django.core.serializers import serialize
from rest_framework import generics
from django.db.models import Avg, Count
from movies.models import Movie
from movies.serializers import MovieSerializer
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.annotate(
        average_rating = Avg("reviews__rating"),
        total_reviews = Count("reviews"),
    )
    serializer_class = MovieSerializer

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.annotate(
        average_rating = Avg("reviews__rating"),
        total_reviews = Count("reviews")
    )
    serializer_class = MovieSerializer
    lookup_field = "tmdb_id"

class MovieReviewsAPIView(APIView):
    def get(self, request, tmdb_id):
        reviews = Review.objects.filter(
            movie__tmdb_id=tmdb_id
        ).select_related("user")

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)