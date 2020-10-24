from django.urls import path
from . import views

urlpatterns = [
    path("", views.photo_index, name="photo_index"),
    
]