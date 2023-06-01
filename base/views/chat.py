from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='base:sign-in')
def chats(request):
   
   context = {
      
   }
   return render(request, 'base/Home.html', context)

@login_required(login_url='base:sign-in')
def chat(request):
   
   context = {
      
   }
   return render(request, 'base/Chat.html', context)
