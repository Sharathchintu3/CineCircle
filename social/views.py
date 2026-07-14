from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Follow
from .serializers import FollowSerializer

class FollowListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Follow.objects.filter(follower = self.request.user).select_related("following")

    def perform_create(self, serializer):
        serializer.save(follower = self.request.user)

class FollowDeleteAPIView(generics.DestroyAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Follow.objects.filter(follower = self.request.user)
