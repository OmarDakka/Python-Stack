from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the equivalent of @app.route('/')")