from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.conf import settings

from movies.models import Movie


class Review(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0.5),
            MaxValueValidator(5)
        ]
    )

    title = models.CharField(
        max_length=200,
    )

    content = models.TextField(
        max_length=1000,
    )

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name = "liked_reviews",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        unique_together = ("user", "movie")

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"

