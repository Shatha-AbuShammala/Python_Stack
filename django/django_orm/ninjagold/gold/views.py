import random
from django.shortcuts import render, redirect


def index(request):

    # if this is the first visit, start gold at 0
    if 'gold' not in request.session:
        request.session['gold'] = 0

    # if this is the first visit, start with empty list of activities
    if 'activities' not in request.session:
        request.session['activities'] = []

    return render(request, 'index.html', {
        'gold': request.session['gold'],
        'activities': request.session['activities']
    })


def process_money(request):

    # get the location from the hidden input in the form
    location = request.POST['location']

    # default values
    amount = 0
    message = ""

    if location == 'farm':
        amount = random.randint(10, 20)
        message = f"You entered a farm and earned {amount} gold."

    elif location == 'cave':
        amount = random.randint(10, 20)
        message = f"You entered a cave and earned {amount} gold."

    elif location == 'house':
        amount = random.randint(10, 20)
        message = f"You entered a house and earned {amount} gold."

    elif location == 'quest':
        amount = random.randint(-50, 50)

        if amount >= 0:
            message = f"You completed a quest and earned {amount} gold."
        else:
            message = f"You failed a quest and lost {abs(amount)} gold. Ouch."

    # update total gold
    request.session['gold'] += amount

    # add new activity to the top of the list
    activities = request.session['activities']
    activities.insert(0, message)
    request.session['activities'] = activities

    return redirect('/')
