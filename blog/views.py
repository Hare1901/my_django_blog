from django.shortcuts import render, get_object_or_404
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

    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )

    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
