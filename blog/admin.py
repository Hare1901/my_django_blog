from django.contrib import admin
from .models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish', 'author']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['author', 'title']
    # автоматическое заполнение из поля title
    prepopulated_fields = {'slug': ('title',)}
    # теперь при заполнении выбираешь из выпадающегно списка
    raw_id_fields = ['author']
    #
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']