from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from machines.models import Machine
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    if request.method == 'POST':
     first_name = request.POST['first_name']  
     last_name = request.POST['last_name']  
     username = request.POST['username']  
     email = request.POST['email']  
     password = request.POST['password']  
     password2 = request.POST['password2'] 
     if password == password2:   
      # user
      if User.objects.filter(username=username).exists():
       messages.error(request, 'Username exist')
       return redirect('register')   
      else:
       if User.objects.filter(email=email).exists():
        messages.error(request, 'email is used')
        return redirect('register')
       else:
        user=User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)   
        user.save()
        messages.success(request, 'you are now registered')
        return redirect('login')
     else:      
      messages.error(request, 'Passwords do not match')
      return redirect('register')
    else:
     return render(request, 'accounts/register.html') 






