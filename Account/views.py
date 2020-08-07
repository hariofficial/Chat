from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone_num = request.POST['phone']

        user = User.objects.create_user(username=username, password=password,email=email,phone_num=phone_num)
        user.save()
        print('user created')
        return redirect('login')

    else:
        return render(request, 'register.html')


def homepage(request):
    return render(request, 'home.html')
