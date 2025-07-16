from django.shortcuts import render, redirect
from .models import Idea
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from devtools.models import Devtool

# Create your views here.
def main_page(request):
    sort = request.GET.get('sort', 'latest')

    if sort == 'name':
        ideas = Idea.objects.all().order_by('title')
    elif sort == 'oldest':
        ideas = Idea.objects.all().order_by('id')
    elif sort == 'liked':
        ideas = Idea.objects.all().order_by('-star')  # True가 먼저
    else:
        ideas = Idea.objects.all().order_by('-id')
    
    context={
        "ideas":ideas,
        "sort":sort,
    }
    return render(request, "main_page.html", context)

def ideas_list(request):
    ideas = Idea.objects.all()
    context = {
        "ideas": ideas
    }
    return render(request, "main_page.html", context)

def ideas_read(request, pk):
    idea = Idea.objects.get(id=pk)
    context = {
        "idea" : idea
    }
    return render(request, "ideas_read.html", context)

def ideas_create(request):
    tools = Devtool.objects.all()

    if request.method == "POST":
        title=request.POST["title"]
        photo=request.FILES.get("photo")
        content=request.POST["content"]
        interest=request.POST["interest"]
        tool_id=request.POST["tool"]
        tool = Devtool.objects.get(id=tool_id)
        Idea.objects.create(
            title=title,
            photo=photo,
            content=content,
            interest=interest,
            tool=tool,
        )
        return redirect("main_page")
    return render(request, "ideas_create.html", {"tools":tools})

def ideas_update(request, pk):
    idea = Idea.objects.get(id=pk)
    tools = Devtool.objects.all()

    if request.method == "POST":
        idea.title = request.POST["title"]
        idea.content = request.POST["content"]
        tool_id = request.POST["tool"]
        idea.tool = Devtool.objects.get(id=tool_id)
        photo = request.FILES.get("photo")
        if photo:
            idea.photo = photo
        idea.interest = request.POST["interest"]
        idea.save()
        return redirect(f"/{pk}")
    
    context = {"idea": idea, "tools": tools}
    return render(request, "ideas_update.html", context)

def ideas_delete(request, pk):
    if request.method == "POST":
        idea = Idea.objects.get(id=pk)
        idea.delete()
    return redirect("main_page")

def star(request, pk):
    idea=Idea.objects.get(id=pk)
    idea.star = not idea.star
    idea.save()
    return JsonResponse({'star':idea.star})

@require_POST
def update_interest(request, pk):
    idea = Idea.objects.get(pk=pk)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "increase":
            idea.interest += 1
        elif action == "decrease" and idea.interest > 0:
            idea.interest -= 1
        idea.save()
        return JsonResponse({"interest":idea.interest})
