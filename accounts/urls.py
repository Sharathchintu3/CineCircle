from django.urls import path
from accounts.views import auth_views

app_name = 'accounts'

urlpatterns = [
    path('register/', auth_views.register, name='register'),
    path('login/', auth_views.user_login, name='login'),
    path('logout/', auth_views.user_logout, name='logout'),
]