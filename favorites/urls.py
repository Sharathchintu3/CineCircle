from django.urls import path
from .views import FavoriteDeleteAPIView, FavoriteListCreateAPIView

urlpatterns = [
    path("", FavoriteListCreateAPIView.as_view(), name="favorite-list-create"),
    path("<int:pk>/", FavoriteDeleteAPIView.as_view(), name="favorite-delete"),
]