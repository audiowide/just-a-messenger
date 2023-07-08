from django.urls import path
from . import views

urlpatterns = [
    path('messages/<str:chat_slug>', views.message_list_create, name='message_list_create'),
    path('messages/<str:chat_slug>', views.message_delete, name='message_delete'),
]
