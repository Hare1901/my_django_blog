
from django.contrib import admin
from django.urls import path, include

from blog.views import post_list

urlpatterns = [
    path('', post_list, name='post_list'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]
