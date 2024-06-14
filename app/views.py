from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout




def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        raw_password=request.POST.get('password')
        user = User.objects.create_user(username, email, raw_password)
        user.save()

        data = User.objects.all()
        print(data)
        
        return render(request,'login.html')
    else:
        return render(request,'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user = authenticate(username=username, password=password)
            print('login successfull')
            if user is not None:

                login(request, user)
                return redirect('/')

        
        else:
            print('something wrong')
            return redirect('/login/')

        
    return render(request, 'login.html')
    


def dashboard_view(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('/login/')
