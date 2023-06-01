from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


def auth(email, password):
   try:
      user = User.objects.get(email=email)
      
      if check_password(password, user.password):
         return user
      return None
   except:
      return None