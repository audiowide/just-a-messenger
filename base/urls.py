from django.urls import path

from .views import auth, chat, user

app_name ='base'

urlpatterns = [
   # sign up
   path('sign-in', auth.sign_in, name='sign-in'),
   path('sign-up', auth.sign_up, name='sign-up'),
   path('sign-out', auth.sign_out, name='sign-out'),
   
   path('', chat.chats, name='chats'),
]
