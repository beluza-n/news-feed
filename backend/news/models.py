from django.db import models
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


class News(models.Model):
    pub_date = models.DateTimeField(
        default=datetime.datetime.now,
        verbose_name='publication date')
    title = models.CharField(max_length=1024, verbose_name='news title')
    text = models.TextField(verbose_name='news text')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='news')

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title


class Comment(models.Model):
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='publication date'
    )
    text = models.TextField(verbose_name='text of the comment')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments')
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='news described in comment'
    )

    def __str__(self):
        return f"{self.author} commented {self.news}"


class Favorites(models.Model):
    user = models.ForeignKey(
        User,
        related_name="favorites",
        on_delete=models.CASCADE)
    news = models.ForeignKey(
        News,
        related_name="favorites",
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'favorites'
        verbose_name_plural = 'favorites'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'news'],
                name="unique_news")
        ]
        ordering = ["-news"]

    def __str__(self):
        return f"{self.user} favorites {self.news}"
