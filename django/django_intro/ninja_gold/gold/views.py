from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    if 'total_gold' not in request.session or 'activities' not in request.session:
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return render(request, 'index.html')

def process_money(request):
    if request.method == "POST":
        if request.POST['building'] == 'farm':
            gold = random.randint(10, 20)
            request.session['activities'].append('You have earned ' + str(gold) + ' golds from the farm' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        if request.POST['building'] == 'cave':
            gold = random.randint(5, 10)
            request.session['activities'].append('You have earned ' + str(gold) + ' golds from the cave' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        if request.POST['building'] == 'house':
            gold = random.randint(2, 5)
            request.session['activities'].append('You have earned ' + str(gold) + ' golds from the house' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
        if request.POST['building'] == 'casino':
            gold = random.randint(-50, 50)
            if gold >= 0:
                request.session['activities'].append('You have earned ' + str(gold) + ' golds from the casino' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
            if gold < 0:
                request.session['activities'].append('You have lost ' + str(gold) + ' golds from the casino' + ' ' + '(' + str(datetime.now().strftime("%Y-%m-%d %H:%M")) + ')')
    
    request.session['total_gold'] += gold
    return redirect('/')

def reset(request):
    if request.method == "GET":
        request.session['total_gold'] = 0
        request.session['activities'] = []
    return redirect('/')