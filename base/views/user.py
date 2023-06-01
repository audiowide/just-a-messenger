from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='base:sign-in')
def settings(request):
   
   return render(request, 'base/Settings.html', context)