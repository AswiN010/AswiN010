from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = auth.authenticate(username=username, password=password)

        if User is not None:
            auth.login(request, User)
            return redirect('/')
        else:
            messages.info(request, "invalid entry")
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                            password=password)
            user.save();
            messages.info(request, 'User is registered')
            return redirect('/')
        else:
            messages.info(request, 'password miss match')
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
