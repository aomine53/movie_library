from cmath import log
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    message = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            message = "Invalid credentials"
    return render(request,'login.html',{'message': message})

def register_view(request):
    message = ""
    is_created = False
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        try:
            user = User.objects.get(username = username)
            message = "Username exists! Try other username."
        except User.DoesNotExist:
            if password1 == password2:
                user = User.objects.create_user(
                username = username,
                password = password1
                )
                message = "Account Created Successfully!"
                is_created = True
            else:
                message = "Passwords do not match!"
             
    return render(request, 'register.html', {'message' : message, 'is_created': is_created})


def logout_view(request):
    logout(request)
    return render(request,'login.html')