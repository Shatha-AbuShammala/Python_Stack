from django.shortcuts import render , redirect

def index(request):
    if 'count' in request.session:
        request.session['count'] +=1
    else:
        request.session['count'] =1 
    return render(request , 'index.html' , {'count': request.session['count']})      


def delete_session(request):
    request.session.flush()
    return redirect ('/')
