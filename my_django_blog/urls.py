
from django.contrib import admin
from django.urls import path, include

from blog.views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]
