from django.shortcuts import render, redirect, get_object_or_404
from . models import Dojo, Ninja
# Create your views here.
def index(request):
    context = {
        "all_the_dojos": Dojo.objects.all(),
        "all_the_ninja": Ninja.objects.all()
    }
    return render(request,"index.html", context)

def add_dojo(request):
    Dojo.objects.create(name = request.POST["dojo_name"], city = request.POST["dojo_city"], state = request.POST["dojo_state"])
    return redirect("/")

def add_ninja(request):
    Ninja.objects.create(first_name= request.POST["first_name"], last_name = request.POST["last_name"], dojo = Dojo.objects.get(name = request.POST['dojo_select']))
    return redirect("/")
   