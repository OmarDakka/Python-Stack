from django.shortcuts import redirect, render
from .models import users

# Create your views here.

def index(request):
    context = {
    	"all_the_users": users.objects.all()
    }
    return render(request, "index.html", context)

def add(request):
    users.objects.create(first_name = request.POST["first_name"], last_name = request.POST["last_name"], email_address = request.POST["email"], age = request.POST["age"])
    return redirect("/")