from rest_framework import serializers

from news.models import News, Comment, Favorites
from users.serializers import CustomUserSerializer



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.email', required=False)
    
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', required=False)
    total_favorite = serializers.IntegerField(read_only=True)
    total_comments = serializers.IntegerField(read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ('id', 'title', 'text', 'author',
                    'pub_date', 'total_favorite',
                    'total_comments', 'comments')

    def get_comments(self, obj):
        request = self.context['request']
        comments_limit = request.query_params.get('comments_limit', 10)
        queryset = (Comment.objects.filter(news_id=obj.id).\
            order_by('-pub_date')[:int(comments_limit)])
        serializer = CommentSerializer(queryset, many=True, read_only=True)
        return serializer.data


class DummyPostNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'text')