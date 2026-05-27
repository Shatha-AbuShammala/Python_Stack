import random
from django.shortcuts import render ,redirect

def index(request):
    if 'number' not in request.session:
        request.session['number']= random.randint(1,100)
        request.session['attempts']= 0
        request.session['message']= ''

    return render(request ,'index.html' ,{'message': request.session.get('message', '')}) 

def guess(request):
    if request.method == "POST":

        guess = int(request.POST['guess'])
        number = request.session['number']

        request.session['attempts'] += 1

        if guess < number:
            request.session['message'] = "Too Low "
        elif guess > number:
            request.session['message'] = "Too High "
        else:
            request.session['message'] = f"Correct , in {request.session['attempts']} tries!"

    return redirect('/')


def reset(request):
    request.session.flush()
    return redirect('/')