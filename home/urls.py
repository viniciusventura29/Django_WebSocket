from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path("register",views.register,name='register'),
    path("login",views.login ,name='login'),
]
