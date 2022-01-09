from django.db import models
import uuid


# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    #profile_image = models.ImageField(blank=True, null=True, upload_to='profiles/', default='profiles/user-default.png')
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.first_name)


class SpokenLanguage(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    score = models.CharField(max_length=200,blank=False,null=False)
    profile = models.ForeignKey(Profile,on_delete=models.SET_NULL)

    def __str__(self):
        return self.name