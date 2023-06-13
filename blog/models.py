from django.db import models
from django.utils import timezone


#представление поста в блоге
class Post(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # сортировка по убыванию
        ordering = ['-publish']
        # определение индексов баз данных
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
