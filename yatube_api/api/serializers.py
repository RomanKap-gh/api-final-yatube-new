from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate(self, data):
        request = self.context.get('request')
        follower = request.user
        following = data['following']

        if following == follower:
            raise serializers.ValidationError(
                'Нельзя подписаться на себя!!')

        if Follow.objects.filter(
            following=following, user=follower
        ).exists():
            raise serializers.ValidationError(
                'Вы уже подписаны на этого пользователя!!'
            )
        return data


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
