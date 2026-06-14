from django.shortcuts import render,redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        # call manager to validate
        errors = User.objects.validator(request.POST)

        # if there is arror
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        
        hashed_pw = bcrypt.hashpw(
            request.POST['password'].encode(),
            bcrypt.gensalt()
        ).decode()

        # create_user
        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_pw
        )

        # session
        request.session['user_id'] = user.id

        return redirect('/success')

    return redirect('/')

def login(request):

    if request.method == 'POST':
        user = User.objects.filter(
            email=request.POST['email']
        ).first()

        if not user:
            messages.error(request, "Invalid email or password")
            return redirect('/')

        # check pass
        if not bcrypt.checkpw(
            request.POST['password'].encode(),
            user.password.encode()
        ):
            messages.error(request, "Invalid email or password")
            return redirect('/')

        # session
        request.session['user_id'] = user.id

        return redirect('/success')

    return redirect('/')

def success(request):

    # protect page
    if 'user_id' not in request.session:
        return redirect('/')

    user = User.objects.get(id=request.session['user_id'])

    return render(request, 'success.html', {
        'user': user
    })

def logout(request):
    request.session.flush()
    return redirect('/')
