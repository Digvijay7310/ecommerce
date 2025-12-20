from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile

# Create your views here.
def signup(request):
    if request.method == "POST":
        user = User.objects.create_user(
            username=request.POST['email'],
            email=request.POST['email'],
            password=request.POST['password'],
            first_name=request.POST['name']
        )
        Profile.objects.create(
            user=user,
            address=request.POST['address'],
            city=request.POST['city'],
            pincode=request.POST['pincode']
        )
        login(request, user)
        return redirect("/")
    return render(request, 'signup.html')

def user_login(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['email'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
           return render(request, 'login.html', {'error': 'Invalid email or password.'})
    else:
        return render(request, 'login.html')
        
def user_logout(request):
    logout(request)
    return redirect("/")