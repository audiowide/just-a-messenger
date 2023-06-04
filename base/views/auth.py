from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User

from ..forms import CreateUserForm
from ..utils import auth

def sign_in(request):
   type = 'sign_in'
   
   if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')
      
      user = auth(email, password)
      
      if user is not None:
         login(request, user)
         return redirect('base:create-chat')
      else:
         messages.error(request, 'Email or password incorrect')
         return redirect('base:sign-in')
   
   context = {
      'page_type': type
   }
   return render(request, 'base/Auth.html', context)

def sign_up(request):
   type = 'sign_up'
   
   if request.method == 'POST':
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')
        
      try:
         isHaveEmail = User.objects.get(email=email)
         
         messages.error(request, 'Email is already exist')
         return redirect('base:sign-in')
      except:
         print('Email does not exist')
         
      try:
         isHaveUsername = User.objects.get(username=username)
         
         messages.error(request, 'Username is already exist')
         return redirect('base:sign-in')
      except:
         print('Username does not exist')
      
      user = User.objects.create(
         username = username,
         email = email,
         password = make_password(password),
      )
         
      login(request, user)
      return redirect('base:create-chat')
   
   context = {
      'page_type': type,
   }
   return render(request, 'base/Auth.html', context)

def sign_out(request):
   logout(request)
   return redirect('base:sign-in')