from django.http.request import HttpRequest
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import redirect, render

def index(request):
    return render(request,'index.html')

def user_info(request):
    request.session['name_from_form'] = request.POST['name']
    request.session['location_from_form'] = request.POST['locations']
    request.session['language_from_form'] = request.POST['language']
    request.session['comments_from_form'] = request.POST['comments']
    context = {
	    "name_temp" : request.session['name_from_form'],
        "location_temp" : request.session['location_from_form'],
        "language_temp" : request.session['language_from_form'],
        "comment_temp" : request.session['comments_from_form'],
    }
    return  redirect("/result")

def result(request):
    context = {
	    "name_temp" : request.session['name_from_form'],
        "location_temp" : request.session['location_from_form'],
        "language_temp" : request.session['language_from_form'],
        "comment_temp" : request.session['comments_from_form'],
    }
    return render(request,"result.html", context)