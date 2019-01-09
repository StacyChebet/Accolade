from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    awardee = models.ForeignKey(User, on_delete=models.CASCADE)
    prof_pic = models.ImageField()
    Bio = models.TextField()
    
