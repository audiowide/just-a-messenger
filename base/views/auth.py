from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate

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
         return redirect('base:chats')
      else:
         messages.error(request,'Email or password incorrect')
         return redirect('base:sign-in')
   
   context = {
      'page_type': type
   }
   return render(request, 'base/Auth.html', context)

def sign_up(request):
   type = 'sign_up'
   form = CreateUserForm()
   
   if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
         form.save()
         
         login(request, user)
         return redirect('base:chats')
   
   context = {
      'page_type': type,
      'form': form,
   }
   return render(request, 'base/Auth.html', context)

def sign_out(request):
   request.logout()
   
   return redirect('base:sign-in')