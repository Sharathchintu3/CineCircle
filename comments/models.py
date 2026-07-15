from typing import reveal_type

from django.db import models
from django.conf import settings

from reviews.models import Review
from reviews.views.api_views import ReviewLikeAPIView


# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    content = models.TextField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} commented on Review {self.review.id}'
