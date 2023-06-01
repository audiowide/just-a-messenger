from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate


def sign_in(request):
   type = 'sign-in'
   
   context = {
      'type': type
   }
   return render(request, 'base/Auth.html', context)

def sign_up(request):
   type = 'sign-up'
   
   
      
   context = {
      'type': type
   }
   return render(request, 'base/Auth.html', context)

def sign_out(request):
   request.logout()
   
   return redirect('base:sign-in')