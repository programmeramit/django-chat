from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "chat.html")
def room(request, room_name,name):
    return render(request, "room.html", {"group_name": room_name,"name":name})
def keys(request):
    return render(request,"keys.html")

