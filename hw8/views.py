from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"user_name": "Deekshit Kalakuntla"}
    return render(request, "index.html", context)
