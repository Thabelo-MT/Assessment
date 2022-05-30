from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if  request.method == "POST":
         username = request.POST['username']
         password = request.POST['password']
         login_user = authenticate(request, username=username, password=password)
         if  login_user is not None:
             login(request, login_user)
             return redirect('index')
         else:
             messages.success(request, ("Please try logging in again.")) 
             return redirect('index')
        
    else:
        return render(request, 'authenticate/index.html', {})
    