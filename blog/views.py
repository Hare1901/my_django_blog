from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post


def post_list(request):

    # published - созданный нами менеджер
    post_list = Post.published.all()
    # Постраничная разбивка по 3 поста на страницу
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


# Пытаемся извлечь объект пост, если возникает ошибка 404 сообщаем что постов не существует
def post_detail(request, year, month, day, post):

    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )

    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
