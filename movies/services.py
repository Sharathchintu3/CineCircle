from .models import Movie, Genre
from .tmdb import TMDBClient


class MovieService:

    def __init__(self):
        self.client = TMDBClient()

    def sync_popular_movies(self):

        data = self.client.get_popular_movies()

        for movie_data in data["results"]:

            movie, created = Movie.objects.update_or_create(
                tmdb_id=movie_data["id"],
                defaults={
                    "title": movie_data["title"],
                    "overview": movie_data["overview"],
                    "poster_path": movie_data["poster_path"] or "",
                    "backdrop_path": movie_data["backdrop_path"] or "",
                    "release_date": movie_data.get("release_date") or None,
                    "original_language": movie_data["original_language"],
                    "popularity": movie_data["popularity"],
                    "vote_average": movie_data["vote_average"],
                    "vote_count": movie_data["vote_count"],
                }
            )

        return True

    def sync_genres(self):

        data = self.client.get_genres()

        for genre in data["genres"]:
            Genre.objects.update_or_create(
                tmdb_id=genre["id"],
                defaults={
                    "name": genre["name"]
                }
            )

        return True