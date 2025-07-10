from django.db import models

# Create your models here.
class Review(models.Model) :
    title = models.CharField(max_length = 32)
    year = models.CharField(max_length = 10)
    genre = models.CharField(max_length = 32)
    score = models.CharField(max_length = 10)
    running_time = models.CharField(max_length = 10)
    content = models.TextField()
    director = models.CharField(max_length = 32)
    actors = models.CharField(max_length = 50)