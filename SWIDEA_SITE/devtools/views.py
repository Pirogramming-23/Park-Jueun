from django.shortcuts import render, redirect
from .models import Devtool
from ideas. models import Idea

def devtools_list(request):
    devtools = Devtool.objects.all()
    context = {
        "devtools":devtools
    }
    return render(request, "devtools_list.html", context)

def devtools_read(request, pk):
    devtool = Devtool.objects.get(id=pk)
    ideas = Idea.objects.filter(tool=devtool)
    context = {
        "devtool":devtool,
        "ideas":ideas,
    }
    return render(request, "devtools_read.html", context)

def devtools_create(request):
    if request.method == "POST":
        Devtool.objects.create(
            name=request.POST["name"],
            kind=request.POST["kind"],
            content=request.POST["content"],
        )
        return redirect("/devtools/")
    return render(request, "devtools_create.html")

def devtools_update(request, pk):
    devtool = Devtool.objects.get(id=pk)

    if request.method == "POST":
        devtool.name = request.POST["name"]
        devtool.kind = request.POST["kind"]
        devtool.content = request.POST["content"]
        devtool.save()
        return redirect(f"/devtools/{pk}")
    context = {"devtool":devtool}
    return render(request, "devtools_update.html", context)

def devtools_delete(request, pk):
    if request.method == "POST":
        devtool = Devtool.objects.get(id=pk)
        devtool.delete()
    return redirect("/devtools/")