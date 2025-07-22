from django.db import models

class Post(models.Model):
    photo = models.ImageField('이미지', blank = False, upload_to='photos/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)