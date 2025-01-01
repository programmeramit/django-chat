from django.urls import path,include
from .views import index,room,keys

urlpatterns = [
    path("",index),
    path("chat/<str:room_name>/<str:name>", room, name="room"),
    path("keys/",keys)
]