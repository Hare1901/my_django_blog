from typing import Dict, Type

from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from blog import views
from blog.sitemaps import PostSitemap



sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    #path('', views.PostListView.as_view(), name='post_list'),
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slut>/', views.post_list, name='post_list_by_tag'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap"
    )

]
