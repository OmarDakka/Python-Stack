from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.
# def index(request):
#     return render(request, 'welcome.html')

def index(request):
    return render(request,'welcome.html')

def root(request):
    return redirect ('/blogs')

def new(request):
    return render(request,'new.html')

def create(request):
    return redirect('/')

def show(request, num):
    return (HttpResponse (f"Blog number {num}"))

def edit(request,num):
    return(HttpResponse (f"edit blog {num}"))

def destroy(request, num):
    return redirect('/')

def jsonmethod(request):
    data = {
        "title": "Omar",
        "content": "yousef"
    }
    return JsonResponse(data)