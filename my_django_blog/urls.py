
from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    #path('', views.PostListView.as_view(), name='post_list'),
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slut>/', views.post_list, name='post_list_by_tag'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
]
