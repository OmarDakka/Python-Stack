from django.shortcuts import render,redirect

# Create your views here.
def main(request):
    if "counter" not in request.session:
        request.session["counter"] =0
    request.session["counter"] += 1 
    context = {
        "temp" : str(request.session["counter"])
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
    print(number_from_form)
    request.session["counter"] += (int(number_from_form) - 1)
    return redirect('/')