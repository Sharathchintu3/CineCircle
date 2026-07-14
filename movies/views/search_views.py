from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer

class MovieSearchAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        query = self.request.GET.get("q")

        if not query:
            return Movie.objects.none()

        return Movie.objects.filter(
            title__icontains=query
        )