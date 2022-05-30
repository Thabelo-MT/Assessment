from tkinter import messagebox
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
#login details fr 3 different people
username = input()
if username == 'Theo' or username== 'Junior' or username =='Tom':
   password = input()
   if username == 'Theo' and password == 'Absa12':
        messagebox.showinfo("You have successfully logged in")
   elif username == 'Junior' and password == 'Jnr@31':
        messagebox.showinfo("You have successfully logged in")
   elif username == 'Tom' and password == 'cod43$':
        messagebox.showinfo("You have successfully logged in")
   else:
        messagebox.showinfo("Your details are incorrect, please try again")
else: 
        messagebox.showinfo("Username does not exists, please sign up")
