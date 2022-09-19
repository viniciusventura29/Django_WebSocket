from importlib.resources import path
from .views import index
from django.urls import path

urlpatterns = [
    path("",index,name="index")
]
