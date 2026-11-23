from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>[1-9]\d*)/comments',
    CommentViewSet,
    basename='CommentList'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
