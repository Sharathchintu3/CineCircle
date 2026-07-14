from django.urls import path
from accounts.views import auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views.profile_views import ProfileAPIView, UpdateProfileAPIView

app_name = 'accounts'

urlpatterns = [
    path('register/', auth_views.register, name='register'),
    path('login/', auth_views.user_login, name='login'),
    path('logout/', auth_views.user_logout, name='logout'),
    path("profile/", ProfileAPIView.as_view(), name="profile"),
    path("profile/update/", UpdateProfileAPIView.as_view(), name="profile-update"),
]

urlpatterns += [
    path(
        "token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),

    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",

    ),
]