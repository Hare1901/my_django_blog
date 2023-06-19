from django.shortcuts import render
from django.http import Http404

from .models import Post


def post_list(request):

    # published - созданный нами менеджер
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


# Пытаемся извлечь объект пост, если возникает ошибка 404 сообщаем что постов не существует
def post_detail(request, id):

    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404('No Post Found')

    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
