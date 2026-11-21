from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from api.serializers import (FollowSerializer, CommentSerializer,
                             GroupSerializer, PostSerializer)
from posts.models import Follow, Group, Post
from .permissions import IsAuthorOrReadOnly


class CreateListViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('pub_date',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = None

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_post().comments.select_related('author')

    def perform_create(self, serializer):
        serializer.save(
            post_id=self.get_post().id,
            author=self.request.user,
        )


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    pagination_class = None

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
        )
