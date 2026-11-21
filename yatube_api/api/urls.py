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
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
