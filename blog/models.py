from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from taggit.managers import TaggableManager



class PublishedManager(models.Manager):
    def get_queryset(self):

        # Возвращается необходимый нам менеджер
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)



#представление поста в блоге
class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "DF", "DRAFT"
        PUBLISHED = "PB", "Published"

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=250,
        choices=Status.choices,
        default=Status.DRAFT

    )
    # Стандартный мессенджер, явно объявили чтобы сохранить
    objects = models.Manager()
    # Конерктно-прикладной мессенджер( созданый нами)
    published = PublishedManager()

    class Meta:
        # сортировка по убыванию
        ordering = ['-publish']
        # определение индексов баз данных
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse(
            "blog:post_details",
            args=[
                self.publish.year,
                self.publish.month,
                self.publish.day,
                self.slug,
                  ]
        )

    tags = TaggableManager()

class Comment(models.Model):

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'