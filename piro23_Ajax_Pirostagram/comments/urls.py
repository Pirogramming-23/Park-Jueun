# comments/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path("create/", comment_create, name="comment_create"),
    path("delete/", comment_delete, name="comment_delete"),
]
