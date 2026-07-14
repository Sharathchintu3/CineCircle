from django.urls import path
from .views import WatchlistListCreateAPIView, WatchlistDeleteAPIView

urlpatterns = [
    path("", WatchlistListCreateAPIView.as_view(), name="watchlist"),
    path("<int:pk>/", WatchlistDeleteAPIView.as_view(), name="watchlist-delete"),
]