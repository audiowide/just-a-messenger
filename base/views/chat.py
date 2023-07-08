from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from ..models import Chat, Message, Profile
from django.contrib.auth.models import User


@login_required(login_url='base:sign-in')
def createChat(request):
   type = 'create'
   
   chats = Chat.objects.filter(Q(user1 =request.user) | Q(user2=request.user))
   
   if request.method == 'POST':
      email = request.POST.get('email')
      
      try: 
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
      'chats': chats
   }
   return render(request, 'base/Chat.html', context)

@login_required(login_url='base:sign-in')
def chat(request, slug):
   type = 'chat'
   
   one_chat = Chat.objects.get(slug=slug)
   
   if request.user == one_chat.user2:
      profile_user2 = Profile.objects.get(user=one_chat.user1)
   else:
      profile_user2 = Profile.objects.get(user=one_chat.user2)
      
   messages = Message.objects.filter(chat=one_chat)
   chats = Chat.objects.filter(Q(user1 =request.user) | Q(user2=request.user))
   
   # if request.method == 'POST':
   #    message = request.POST.get('message')
      
   #    message = Message.objects.create(
   #       chat = one_chat,
   #       user = request.user,
   #       message = message,
   #    )
   #    return redirect('base:chat', one_chat.slug)
         
   context = {
      'type': type,
      
      'one_chat': one_chat,
      'profile_user2': profile_user2,
      
      'chats': chats,
   }
   return render(request, 'base/Chat.html', context)

@login_required(login_url='base:sign-in')
def message_delete(request, slug, message_id):
   try:
      one_chat = Chat.objects.get(slug=slug)
      message = Message.objects.get(id=message_id)
      
      if message.user == request.user:
         message.delete()
         return redirect('base:chat', one_chat.slug)
         
   except:
      message.error(request, 'message not found')
      return redirect('base:chat', one_chat.slug)
      
@login_required(login_url='base:sign-in')
def chat_delete(request, slug):
   try:
      one_chat = Chat.objects.get(slug=slug)
      
      if one_chat.user1 == request.user or one_chat.user2 == request.user:
         messages = Message.objects.filter(chat=one_chat)
         
         for message in messages:
            message.delete()
         
         one_chat.delete()
         return redirect('base:create-chat')
         
   except:
      message.error(request, 'chat not found')
      return redirect('base:create-chat')