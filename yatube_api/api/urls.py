from django.urls import include, path
from rest_framework import routers

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('follow', FollowViewSet, basename='v1-follow')
router_v1.register('groups', GroupViewSet, basename='v1-group')
router_v1.register('posts', PostViewSet, basename='v1-post')
router_v1.register(
    r'posts/(?P<post_id>[1-9]\d*)/comments',
    CommentViewSet,
    basename='v1-comment'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
