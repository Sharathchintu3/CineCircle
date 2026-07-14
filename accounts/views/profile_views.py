from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from accounts.models import Profile
from accounts.serializers import ProfileSerializer

class ProfileAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile


class UpdateProfileAPIView(generics.UpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
