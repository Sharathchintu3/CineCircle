from django.conf import settings
from django.db import models

from movies.models import Movie


class Watchlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="watchlist",
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="watchlisted_by",
    )

    added_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'