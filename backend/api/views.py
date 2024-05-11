from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiExample

from .pagination import CustomPageNumberPagination
from news.models import News, Comment, Favorites
from .serializers import NewsSerializer, CommentSerializer, DummyPostNewsSerializer
from .permissions import NewsPermission


@extend_schema(tags=["News"])
@extend_schema_view(
    list=extend_schema(
        summary="Список новостей",
        parameters=[
            OpenApiParameter(
                name='comments_limit',
                location=OpenApiParameter.QUERY,
                description='Количество комментариев к новости',
                required=False,
                type=int
            ),
        ]
    ),
    create=extend_schema(
        summary="Создать новость",
        request=DummyPostNewsSerializer,
    ),
    update=extend_schema(
        summary="Обновить новость",
        request=DummyPostNewsSerializer,
    ),
    retrieve=extend_schema(summary="Посмотреть одну новость"),
    destroy=extend_schema(summary="Удалить новость"),

)
class NewsViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'head', 'option']
    serializer_class = NewsSerializer
    permission_classes = (NewsPermission,)
    pagination_class = CustomPageNumberPagination
    ordering = ('-pub_date',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        user_id = user.id if not user.is_anonymous else None
        queryset = News.objects.all().annotate(
            total_favorite=Count(
                "favorites",
                filter=Q(favorites__user_id=user_id)
            )
        )
        queryset = queryset.annotate(
            total_comments=Count(
                "comments",
                filter=Q(comments__author_id=user_id)
            )
        )
        return queryset.order_by('-pub_date')


@extend_schema(tags=["Comments"])
@extend_schema_view(
    list=extend_schema(summary="Список комментариев"),
    create=extend_schema(summary="Создать комментарий"),
    retrieve=extend_schema(summary="Посмотреть один комментарий"),
    destroy=extend_schema(summary="Удалить коментарий"),

)
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (NewsPermission,)
    http_method_names = ['get', 'post', 'delete']

    def get_news(self):
        news_id = self.kwargs.get('news_id')
        return get_object_or_404(News, pk=news_id)

    def get_queryset(self):
        return self.get_news().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            news=self.get_news()
        )

@extend_schema(tags=["Favorites"])
@extend_schema_view(
    post=extend_schema(
        summary="Добавить новость в избранное",
        responses={
            status.HTTP_201_CREATED: NewsSerializer,
        },
    ),
    delete=extend_schema(
            summary="Удалить новость из избранного",
        ),
)
class FavoritesAPIView(APIView):
    """
    Add or remove news from favorites.
    """
    permission_classes = (IsAuthenticated, )

    def post(self, request, pk):
        self.check_permissions(request)
        user = request.user
        try:
            news = News.objects.get(pk=pk)
        except News.DoesNotExist:
            return Response(
                {'детали': 'Новости не существует.'},
                status=status.HTTP_400_BAD_REQUEST)
        if Favorites.objects.filter(user=user, news=news).exists():
            return Response(
                {'детали': 'Уже в избранном'},
                status=status.HTTP_400_BAD_REQUEST)
        else:
            Favorites.objects.create(user=user, news=news)

        serializer = NewsSerializer(news, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        self.check_permissions(request)
        user = request.user
        news = get_object_or_404(News, pk=pk)
        try:
            Favorites.objects.get(user=user, news=news).delete()
        except Favorites.DoesNotExist:
            return Response(
                {'детали': 'Новость не в избранном'},
                status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)