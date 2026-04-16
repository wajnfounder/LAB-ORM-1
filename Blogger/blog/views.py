from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Blog


def home_view(request: HttpRequest):
    posts = Blog.objects.filter(is_published=True).order_by('-published_at')
    posts = Blog.objects.filter(is_published=True).order_by('-published_at')
    return render(request, "blog/home.html", {"posts": posts})


def create_post_view(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        

        Blog.objects.create(
            title=title,
            content=content,
            image=image
        )

        return redirect("blog:home")
    return render(request, "blog/create.html")

def post_detail_view(request, id):
    post = Blog.objects.get(id=id)
    return render(request, "blog/detail.html", {"post": post})

def edit_post_view(request, id):
    post = Blog.objects.get(id=id)

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()

        return redirect("blog:post_detail", id=post.id)

    return render(request, "blog/edit.html", {"post": post})

def delete_post_view(request, id):
    post = Blog.objects.get(id=id)
    post.delete()

    return redirect("blog:home")

