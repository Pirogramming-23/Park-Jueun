from django.db import models

class Idea(models.Model):
    title = models.CharField(max_length=32)
    tool = models.ForeignKey("devtools.DevTool", on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField('이미지', blank=True)
    interest = models.IntegerField(default=0)
    content = models.TextField(default="")
    star = models.BooleanField(default=False)

