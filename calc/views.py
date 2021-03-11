from django.shortcuts import render, redirect
from django.contrib  import messages
from django.contrib.auth.models import User, auth
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password=request.POST['pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            print('LOGIN')
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'assignment-html.html')

    else:
        return render(request, 'assignment-html.html')



def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken')
            print('NOT CREATED')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email taken')
            print('NOT CREATED')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            print('created')
            return render(request, 'home.html')
    else:
        return render(request, 'assignment-html.html')
    

    