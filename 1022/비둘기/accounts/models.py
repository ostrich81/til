from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    followers= models.ManyToManyField('self',symmetrical=False, related_name='followings')
    from_user_id=models.IntegerField()
    to_user_id=models.IntegerField()

class Community(models.Model):
    password=models.CharField(max_length=128)
    username=models.CharField(max_length=150)
    email=models.CharField(max_length=254)
    is_superuser = models.BooleanField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    last_name=models.CharField(max_length=150)
    first_name=models.CharField(max_length=150)


