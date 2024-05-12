from rest_framework import routers
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView)

from .views import (
    NewsViewSet,
    CommentViewSet,
    FavoritesAPIView)

v1_router = routers.DefaultRouter()
v1_router.register(r'news', NewsViewSet, basename='news')
v1_router.register(
    r'news/(?P<news_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('', include(v1_router.urls)),
    path('news/<int:pk>/favorite/', FavoritesAPIView.as_view()),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(
        url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(
        url_name='schema'), name='redoc'),
]
