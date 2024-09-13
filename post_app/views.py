from rest_framework import status
from .models import Post, Like, Follow, Comment
from .serializers import PostSerializer, LikeSerializer, FollowSerializer, CommentSerializer
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
    ListCreateAPIView,
)

class Unfollow(DestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    def


class LikeList(ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeListSerializer
