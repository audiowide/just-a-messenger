from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

from ..models import Chat, Profile
from django.contrib.auth.models import User


@login_required(login_url='base:sign-in')
def settings(request):
   type = 'settings'
   
   user = User.objects.get(id=request.user.id)
   profile = Profile.objects.get(user=user)
   
   chats = Chat.objects.filter(Q(user1 =request.user) | Q(user2=request.user))
   
   if request.method == 'POST':
      email = request.POST.get('email')
      username = request.POST.get('username')
      image = request.FILES.get('image')
      about = request.POST.get('about')
      
      if email != user.email: user.email = email
      if username != user.username: user.username = username
      if image: profile.image = image
      if about != profile.about: profile.about = about
      
      user.save()
      profile.save()
      return redirect('base:settings')
   
   context = {
      'type': type,
      
      'chats': chats,
      'profile': profile,
   }
   return render(request, 'base/Chat.html', context)