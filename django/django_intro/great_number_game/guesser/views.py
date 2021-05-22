from django.shortcuts import render,HttpResponse
import random


def main(request):
    if "attempt" in request.session:
        del request.session["attempt"]
    if "number" not in request.session:
        request.session['number'] = 0
    if "attempt" not in request.session:
        request.session['attempt'] = 0
    request.session['number'] = random.randint(1,100)
    return render(request,"result.html")

def show(request):
    guessing = request.POST["guess"]
    request.session["guessingAgain"] = guessing
    if request.session['number'] > int(request.session["guessingAgain"]):
        request.session["answer"] = "Too Low"
    if request.session['number'] < int(request.session["guessingAgain"]):
        request.session["answer"] = "Too High"
    if request.session['number'] == int(request.session["guessingAgain"]):
        request.session["answer"] = "Correct"
    request.session["attempt"] += 1
    context = {
        "number" : request.session["number"],
        "firstGuess" : request.session["answer"],
        "attempts" : request.session["attempt"]
    }
    
    return render(request,"result.html", context)
