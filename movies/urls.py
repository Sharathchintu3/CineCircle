from django.urls import path

from movies.views.api_views import MovieListAPIView, MovieDetailAPIView, MovieReviewsAPIView
from movies.views.search_views import MovieSearchAPIView

app_name = "movies"

urlpatterns = [
    path("api/movies/", MovieListAPIView.as_view(), name = "movie-list"),
path(
        "api/movies/search/",
        MovieSearchAPIView.as_view(),
        name="movie-search"
    ),
    path("api/movies/<int:tmdb_id>/reviews/",
         MovieReviewsAPIView.as_view(),
         name="movie_reviews"),
    path("api/movies/<int:tmdb_id>/",
         MovieDetailAPIView.as_view(),
         name = "movie-details"
    ),

]
