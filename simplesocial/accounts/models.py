from django.db import models
from django.contrib import auth


# Create your models here.
# Going to use Django's models
class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username) # username is a builtin attribute that comes with .User (fn, ln, email, etc.)
        #now creating a view 
