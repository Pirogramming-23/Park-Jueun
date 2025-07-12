from django.shortcuts import render, redirect
from .models import Review

def reviews_list(request):
    reviews = Review.objects.all()
    context = {
        "reviews":reviews
    }
    return render(request, "reviews_list.html", context)

def reviews_read(request, pk):
    review = Review.objects.get(id=pk)
    context = {
        "review":review
    }
    return render(request, "reviews_read.html", context)

def reviews_create(request):
    if request.method == "POST" :
        Review.objects.create(
            title=request.POST["title"],
            year=request.POST["year"],
            genre=request.POST["genre"],
            score=request.POST["score"],
            running_time=request.POST["running_time"],
            content=request.POST["content"],
            director=request.POST["director"],
            actors=request.POST["actors"],
        )
        return redirect("/")
    return render(request, "reviews_create.html")

def reviews_update(request, pk):
    review = Review.objects.get(id=pk)

    if request.method == "POST":
        review.title = request.POST["title"]
        review.year = request.POST["year"]
        review.genre = request.POST["genre"]
        review.score = request.POST["score"]
        review.running_time = request.POST["running_time"]
        review.content = request.POST["content"]
        review.director = request.POST["director"]
        review.actors = request.POST["actors"]
        review.save()
        return redirect(f"/{pk}")
    
    context = {"review":review}
    return render(request, "reviews_update.html", context)

def reviews_delete(request, pk):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/")