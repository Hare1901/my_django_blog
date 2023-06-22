from django.urls import path

from . import views




app_name = 'blog'

# Представление поста
urlpatterns = [
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
         views.post_detail,
         name='post_details'
         ),
]