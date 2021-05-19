from django.shortcuts import render,redirect

# Create your views here.
def main(request):
    if "counter" not in request.session:
        request.session["counter"] = 0
    if "views" not in request.session:
        request.session["views"] = 0
    request.session["counter"] += 1 
    request.session["views"] += 1 
    context = {
        "counter" : str(request.session["counter"]),
        "views" : str(request.session["views"])  
    }
    return render(request, "index.html", context)

def addTwo(request):
    request.session["counter"] += 1
    return redirect ("/")

def destroy(request):
    del request.session["counter"]
    return redirect('/')

def add(request):
    number_from_form = request.POST["number"]
    request.session["counter"] += (int(number_from_form) - 1)
    return redirect('/')