from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..models import Chat, Message
from django.contrib.auth.models import User


@login_required(login_url='base:sign-in')
def createChat(request):
   type = 'create'
   
   if request.method == 'POST':
      email = request.POST.get('email')
      
      # try: 
      guest = User.objects.get(email=email)
      
      slug_massive  = [guest.username, request.user.username]
      slug_massive.sort()
      slug = f'{slug_massive[0]}-{slug_massive[1]}'
      
      try:
         isHaveChat = Chat.objects.get(slug=slug)
         return redirect('base:chat', isHaveChat.slug)
      except Chat.DoesNotExist:
         chat = Chat.objects.create(slug=slug, user1=request.user, user2=guest)
         return redirect('base:chat', chat.slug)
      
      except:
         messages.error(request, 'User not found')
            
   context = {
      'type': type,
   }
   return render(request, 'base/Chat.html', context)

@login_required(login_url='base:sign-in')
def chat(request, slug):
   type = 'chat'
   
   one_chat = Chat.objects.get(slug=slug)
   messages = Message.objects.filter(chat=one_chat)
   
   if request.method == 'POST':
      message = request.POST.get('message')
      
      message = Message.objects.create(
         chat = one_chat,
         user = request.user,
         message = message,
      )
      return redirect('base:chat', one_chat.slug)
         
   context = {
      'type': type,
      'one_chat': one_chat,
      'texts': messages
   }
   return render(request, 'base/Chat.html', context)
