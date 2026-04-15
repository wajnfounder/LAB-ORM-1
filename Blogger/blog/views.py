from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Blog


def home_view(request: HttpRequest):
    posts = Blog.objects.filter(is_published=True).order_by('-published_at')
    return render(request, "blog/home.html", {"posts": posts})


def create_post_view(request: HttpRequest):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        Blog.objects.create(
            title=title,
            content=content
        )

        return redirect("blog:home")

    return render(request, "blog/create.html")

def delete_post_view(request, id):
    post = Blog.objects.get(id=id)
    post.delete()
    return redirect('blog:home')

def edit_post_view(request, id):
    post = Blog.objects.get(id=id)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()

        return redirect('blog:home')

    return render(request, "blog/edit.html", {"post": post})
