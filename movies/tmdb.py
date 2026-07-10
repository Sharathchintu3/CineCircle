import requests
from django.conf import settings

BASE_URL = "https://api.themoviedb.org/3"


class TMDBClient:

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {settings.TMDB_ACCESS_TOKEN}",
            "accept": "application/json"
        }

    def get_popular_movies(self, page=1):

        url = f"{BASE_URL}/movie/popular"

        response = requests.get(
            url,
            headers=self.headers,
            params={"page": page}
        )

        response.raise_for_status()

        return response.json()

    def search_movies(self, query):

        url = f"{BASE_URL}/search/movie"

        response = requests.get(
            url,
            headers=self.headers,
            params={
                "query": query
            }
        )

        response.raise_for_status()

        return response.json()

    def get_movie_details(self, tmdb_id):

        url = f"{BASE_URL}/movie/{tmdb_id}"

        response = requests.get(
            url,
            headers=self.headers
        )

        response.raise_for_status()

        return response.json()

    def get_genres(self):
        url = f"{BASE_URL}/genre/movie/list"

        response = requests.get(
            url,
            headers=self.headers
        )

        response.raise_for_status()

        return response.json()