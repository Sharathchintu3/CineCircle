from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from reviews.permissions import IsReviewOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewUpdateAPIView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsReviewOwner]

class ReviewDeleteAPIView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsReviewOwner]

class ReviewLikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        review = generics.get_object_or_404(Review, pk = pk)
        if review.likes.filter(id=request.user.id).exists():
            return Response(
                {"message":"You already liked this review."},
                status = status.HTTP_400_BAD_REQUEST,
            )
        review.likes.add(request.user)

        return Response(
            {"message":"Review liked successfully."},
            status = status.HTTP_200_OK,
        )