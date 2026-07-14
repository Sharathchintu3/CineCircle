from datetime import datetime
from .models import Movie, Genre
from .tmdb import TMDBClient


class MovieService:

    def __init__(self):
        self.client = TMDBClient()

    def sync_genres(self):
        data = self.client.get_genres()

        for genre in data["genres"]:
            Genre.objects.update_or_create(
                tmdb_id=genre["id"],
                defaults={
                    "name": genre["name"]
                }
            )

    def sync_popular_movies(self):

        data = self.client.get_popular_movies()

        for movie_data in data["results"]:

            release_date = None
            if movie_data.get("release_date"):
                release_date = datetime.strptime(
                    movie_data["release_date"],
                    "%Y-%m-%d"
                ).date()

            movie, created = Movie.objects.update_or_create(
                tmdb_id=movie_data["id"],
                defaults={
                    "title": movie_data["title"],
                    "overview": movie_data["overview"],
                    "poster_path": movie_data.get("poster_path") or "",
                    "backdrop_path": movie_data.get("backdrop_path") or "",
                    "release_date": release_date,
                    "original_language": movie_data["original_language"],
                    "popularity": movie_data["popularity"],
                    "vote_average": movie_data["vote_average"],
                    "vote_count": movie_data["vote_count"],
                }
            )

            movie.genres.clear()

            for genre_id in movie_data["genre_ids"]:
                try:
                    genre = Genre.objects.get(tmdb_id=genre_id)
                    movie.genres.add(genre)
                except Genre.DoesNotExist:
                    continue

        return True