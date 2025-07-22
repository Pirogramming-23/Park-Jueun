from django.shortcuts import render, HttpResponse, redirect
from .models import Post

def main_page(request):
    posts = Post.objects.all()
    context = {
        "posts":posts
    }
    return render(request, "main_page.html", context)

def posts_read(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        "post":post
    }
    return render(request, "posts_read.html",context)

def posts_create(request):
    if request.method == "POST":
        Post.objects.create(
            photo = request.FILES.get('photo'),
            content = request.POST['content'],
        )
        return redirect("main_page")
    return render(request, "posts_create.html")

from django.http import JsonResponse

def post_like(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        post = Post.objects.get(id=post_id)

        # 좋아요 토글: 0이면 1, 1이면 0
        if post.like == 0:
            post.like = 1
        else:
            post.like = 0

        post.save()
        return JsonResponse({'like': post.like})