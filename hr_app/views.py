

# Create your views here.
# hr_app/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the HR Project! Your app is live!</h1>")
