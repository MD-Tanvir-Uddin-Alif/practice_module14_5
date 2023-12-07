from django.urls import path
from .import views

urlpatterns = [
    path("",views.home),
    path("modal/",views.modal),
]