from idlelib.debugobj_r import remote_object_tree_item
from typing import reveal_type

from rest_framework import serializers
from rest_framework.views import set_rollback

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField()
    favorites_count = serializers.SerializerMethodField()
    watchlist_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile


        fields = [
            "username",
            "email",
            "profile_picture",
            "bio",
            "location",
            "created_at",
            "followers_count",
            "following_count",
            "reviews_count",
            "favorites_count",
            "watchlist_count",
        ]
    def get_followers_count(self,obj):
        return obj.user.followers.count()

    def get_following_count(self,obj):
        return obj.user.following.count()

    def get_reviews_count(self,obj):
        return obj.user.reviews.count()

    def get_favorites_count(self, obj):
        return obj.user.favorites.count()

    def get_watchlist_count(self, obj):
        return obj.user.watchlist.count()

