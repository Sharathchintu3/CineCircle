from django.urls import path
from .views import FollowListCreateAPIView, FollowDeleteAPIView

urlpatterns =[
    path("",
         FollowListCreateAPIView.as_view(),
         name="follow-list-created"),
    path("<int:pk>/",
         FollowDeleteAPIView.as_view(),
         name="follow-delete"),
]