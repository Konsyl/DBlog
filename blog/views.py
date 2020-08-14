from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post
from blog.forms import PostForm
from django.utils import timezone


def show_post_list(request):
    posts = Post.objects.all()[::-1]
    return render(request, 'post_list.html', {'posts': posts})


def get_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_read.html', {'post': post})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('/blog', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})
