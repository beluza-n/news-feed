from django.contrib import admin

from .models import News, Comment, Favorites

admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Favorites)
