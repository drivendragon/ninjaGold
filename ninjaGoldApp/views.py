from django.shortcuts import render, redirect
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, "index.html")

def process_money(request):
    print("form submitted")
    print(request.POST)
    if request.POST['building'] == 'farm':
        print("farm visited")
        num = random.randint(10,20)
        request.session['gold'] += num
        request.session['activities'].append("You earned " + str(num) + "! Yay!")
    elif request.POST['building'] == 'cave':
        print('cave visited')
        num = random.randint(5,10)
        request.session['gold'] += num
        request.session['activities'].append("You earned " + str(num) + "! Yay!")
    elif request.POST['building'] == 'house':
        print('house visited')
        num = random.randint(2,5)
        request.session['gold'] += num
        request.session['activities'].append("You earned " + str(num) + "! Yay!")
    elif request.POST['building'] == 'casino':
        print('casino visited')
        num =  random.randint(-50,50)
        if num >= 0:
            request.session['activities'].append("You earned nothing " + str(num) + "! Yay!")
        elif num == 0:
            request.session['activities'].append("You earned nothing nothing.")
        else:
            request.session['activities'].append("You lossed " + str(abs(num)) + "! Boooo!")

        request.session['gold'] += random.randint(-50,50)
    print('You now have ' + str(request.session['gold']) + ' gold')
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')