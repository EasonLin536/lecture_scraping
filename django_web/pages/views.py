from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about me.",
        "my_list": ["Eason", "NTU", "Electrical Engineering"]
    }
    return render(request, "about.html", my_context)