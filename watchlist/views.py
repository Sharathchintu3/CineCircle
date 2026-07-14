from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from .models import Watchlist
from .serializers import WatchlistSerializer

class WatchlistListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Watchlist.objects.filter(user = self.request.user).select_related("movie")

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class WatchlistDeleteAPIView(generics.DestroyAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Watchlist.objects.filter(user = self.request.user)