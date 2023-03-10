from http.client import HTTPResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Contact

def home(request):
    return render(request,'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fullname = request.POST['fullname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        myuser = User.objects.create_user(username,email,pass1)
        splitted_name = fullname.split()
        myuser.first_name= splitted_name[0]
        myuser.last_name= splitted_name[-1]
        if pass1 != pass2:
            messages.error(request,'Passwords did not match!')
            return redirect('home')
        else:
            myuser.save()
            messages.success(request, "Signed up successfully!")
            return redirect('home')
    else:
        return HttpResponse('404 -Not Found!')

def signin(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid credentials!')
            return redirect('home')
    return redirect('home')

def signout(request):
    logout(request)
    messages.success(request,'Signed out successfully!')
    return redirect('home')

def iomcourse(request):
    return render(request,'comingsoon.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        messages.success(request,"Message sent!")
        return redirect('home')
    else:
        return HttpResponse('404 -Not Found!')


