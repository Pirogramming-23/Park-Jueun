from django.db import models

class Devtool(models.Model):
    name = models.CharField(max_length=32)
    kind = models.CharField(max_length=32)
    content = models.TextField(default="")
    
    def __str__(self):
        return self.name