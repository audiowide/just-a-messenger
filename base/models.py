from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Profile(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
   
   image = models.ImageField(upload_to='profile', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'svg', 'gif'])], blank=True)
   about = models.TextField(blank=True, max_length=100)
   
   blocked_users = models.ManyToManyField(User, blank=True, related_name='blocked_users')
   
   def __str__(self):
       return self.user.username
   
class Chat(models.Model):
   name = models.CharField(max_length=100)
   slug = models.CharField(max_length=100, unique=True)
   
   def __str__(self):
       return self.slug
    
class Message(models.Model):
   chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   
   message = models.TextField(max_length=10000)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return '{} - {} - {}'.format(self.chat.name, self.user.username, created)
   