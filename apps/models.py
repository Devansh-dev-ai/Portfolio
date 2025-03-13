from django.db import models

# Create your models here.
class Owner(models.Model):
    OwerName = models.CharField(max_length= 20, default="Devansh Durgapal")
    OwnerImage = models.ImageField(upload_to = 'images/UserImage')

class ContactToUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact_phone = models.IntegerField()
    message = models.TextField() 

class UserProjects(models.Model):
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=50)
    github_link = models.URLField(max_length=200)
    project_picture = models.ImageField(upload_to = 'image/ProjectsImages')

class UserResume(models.Model):
    file = models.FileField()
    date_update = models.DateTimeField(auto_now_add= True)