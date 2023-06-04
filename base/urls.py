from django.urls import path

from .views import auth, chat, user

app_name ='base'

urlpatterns = [
   # sign up
   path('sign-in', auth.sign_in, name='sign-in'),
   path('sign-up', auth.sign_up, name='sign-up'),
   path('sign-out', auth.sign_out, name='sign-out'),
   
   path('settings', user.settings, name='settings'),
   
   path('create-chat', chat.createChat, name='create-chat'),
   path('chats/<str:slug>', chat.chat, name='chat'),
   
   path('chats/<str:slug>/delete', chat.chat_delete, name='chat-delete'),
   path('chats/<str:slug>/messages/<int:message_id>/', chat.message_delete, name='message-delete'),
]
