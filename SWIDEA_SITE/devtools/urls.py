from django.urls import path
from .views import *
from django.shortcuts import render

urlpatterns = [
    path('', devtools_list),
    path('<int:pk>/', devtools_read, name="devtools_read"),
    path('create/', devtools_create, name="devtools_create"),
    path('<int:pk>/update/', devtools_update),
    path('<int:pk>/delete/', devtools_delete),
]