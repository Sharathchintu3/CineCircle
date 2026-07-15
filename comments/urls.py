from django.urls import path
from .views import CommentListCreatedAPIView, CommentDeleteAPIView

urlpatterns = [
    path("reviews/<int:review_id>/comments/",
         CommentListCreatedAPIView.as_view(),
         name="comment-list-created"),
    path("comments/<int:pk>/",
         CommentDeleteAPIView.as_view(),
         name = "comment-delete"),
]