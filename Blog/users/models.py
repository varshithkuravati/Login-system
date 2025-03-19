from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField('email adress',unique=True)
    # username = models.CharField(max_length=100,default=None)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]
    
class Profile(models.Model):
    about = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='static/images')
    user = models.OneToOneField(User,on_delete= models.CASCADE)


