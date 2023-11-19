from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"user_name": "Bhaskar Reddy Kodala"}
    return render(request, "index.html", context)
