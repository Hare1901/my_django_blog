from django.urls import path

from . import views
from .feeds import LatestPostsFeed




app_name = 'blog'

# Представление поста
urlpatterns = [
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
         views.post_detail,
         name='post_details'
         ),
    path(
        '<int:post_id>/share/',
        views.post_share,
        name='post_share'
        ),
    path(
        "<int:post_id>/comment",
        views.post_comment,
        name='post_comment'
        ),
    path('feed/',
        LatestPostsFeed(),
        name='post_feeds'
         )
]