from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name="main_page"),
    path("<int:pk>/", ideas_read),
    path('<int:pk>/star/', star),
    path('<int:pk>/interest/', update_interest, name='update_interest'),
	path('create/', ideas_create),
    path('<int:pk>/update/', ideas_update),
    path('<int:pk>/delete/', ideas_delete),
]