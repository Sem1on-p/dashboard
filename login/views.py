from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def autentificated(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'GET':
            return render(request, 'registration/login.html')

        elif request.method == 'POST':
            username = request.POST['username'].lower()
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
    return render(request, 'registration/login.html')

