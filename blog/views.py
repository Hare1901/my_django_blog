from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.decorators.http import require_POST

from .models import Post, Comment
from .forms import EmailPostForm, CommentFrom
from my_django_blog.config import *

class PostListView(ListView):

    #указываем конкретный набор qweryset, по умолчанию Post.object.all()
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


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


def post_share(request, post_id):
    # Извлекаем пост по id
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )

    sent = False

    # Передача на обработку формы
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read"\
                      f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n"\
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, email, [cd['to']])
            sent = True
    else:
        form = EmailPostForm()

    return render(
        request,
        'blog/post/share.html',
        {
            'post': post,
            'form': form,
            'sent': sent
        }
    )



@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )

    comment = None
    # заполняется форма комментария
    form = CommentFrom(data=request.POST)
    # Проверяем на валидность данные с формы
    if form.is_valid():
        # Создаем обект класса, пока не сохраняя его
        comment = form.save(commit=False)
        # привязываем коментарий к посту
        comment.post = post
        comment.save()

    return render(
        request,
        'blog/post/comment.html',
        {
            'post': post,
            'form': form,
            'comment': comment

        }
    )
