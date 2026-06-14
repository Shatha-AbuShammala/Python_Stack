from django.shortcuts import render,redirect
from .models import Dojo , Ninja

def index(request):
    context ={
        'dojos': Dojo.objects.all(),
    }
    return render(request,'index.html',context)

def create_dojo(request):
    if request.method == 'POST':
        Dojo.objects.create(
        name = request.POST['name'],
        city= request.POST['city'],
        state = request.POST['state']
    )
    return redirect('/')

def create_ninga(request):
    if request.method == 'POST':
        Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name= request.POST['last_name'],
        dojo = Dojo.objects.get(id=request.POST['dojo_id'])
    )
    return redirect('/')

#

