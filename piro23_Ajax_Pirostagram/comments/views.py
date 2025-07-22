# comments/views.py
from django.http import JsonResponse
from .models import Comment
from posts.models import Post

def comment_create(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        content = request.POST.get("content")
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(post=post, content=content)
        return JsonResponse({
            "content": comment.content,
            "created_at": comment.created_at.strftime("%Y-%m-%d %H:%M"),
            "id": comment.id, 
        })

def comment_delete(request):
    if request.method == "POST":
        comment_id = request.POST.get("comment_id")
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return JsonResponse({'status': 'ok'})
        except Comment.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Not found'}, status=404)