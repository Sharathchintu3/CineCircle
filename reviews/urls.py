from django.urls import path
from reviews.views.api_views import ReviewCreateAPIView, ReviewUpdateAPIView, ReviewDeleteAPIView, ReviewLikeAPIView

urlpatterns = [
    path("", ReviewCreateAPIView.as_view(), name="review-create"),
    path("<int:pk>/", ReviewUpdateAPIView.as_view(), name="review-update"),
    path("<int:pk>/delete/", ReviewDeleteAPIView.as_view(), name="review-delete"),
    path("<int:pk>/like/", ReviewLikeAPIView.as_view(), name="review-like"),
]