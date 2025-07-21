from django.urls import path
from .views import *

urlpatterns = [
    path("", main_page),
    path("<int:pk>/", posts_read),
    path("create/", posts_create),
    path("like/", post_like, name="like"),
]