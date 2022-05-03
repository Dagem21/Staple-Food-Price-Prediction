from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return render(request, 'sfppApp/predictions.html')

def login(request):

    if request.method == 'POST':
        phonenum = request.POST['phonenumber']
        password = request.POST['password']

        print(phonenum, password)

        messages.success(request, "Login Successful!")

        return redirect('/')

    return render(request, 'sfppApp/login.html')

def register(request):

    if request.method == 'POST':
        phonenum = request.POST['phonenumber']
        username = request.POST['username']
        password = request.POST['password']
        confpass = request.POST['confirmpassword']

        print(phonenum, username, password, confpass)

        messages.success(request, "Registration completed!")

        return redirect('/login')

    return render(request, 'sfppApp/signup.html')

def logout(request):
    return render(request, 'sfppApp/predictions.html')