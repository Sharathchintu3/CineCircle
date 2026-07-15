from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from reviews.models import Review
from .permissions import IsCommentOwner
# Create your views here.
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreatedAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        review_id = self.kwargs["review_id"]
        return Comment.objects.filter(
            review_id=review_id
        ).select_related("user")

    def perform_create(self, serializer):
        review = generics.get_object_or_404(
            Review,
            pk = self.kwargs["review_id"]
        )

        serializer.save(
            user = self.request.user,
            review=review
        )

class CommentDeleteAPIView(generics.DestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsCommentOwner]

    queryset = Comment.objects.all()