from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    awardee = models.ForeignKey(User, on_delete=models.CASCADE)
    prof_pic = models.ImageField()
    Bio = models.TextField()

class Project(models.Model):
    awardee = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=40)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    def save_project(self):
        self.save()
    
    @classmethod
    def get_all_projects(self):
        projects = Project.objects.all()
        return projects