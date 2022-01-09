from django.db import models
import uuid
from profiles.models import Profile


# Create your models here.

class Testimonial(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
    author_name = models.CharField(max_length=200, blank=False, null=False)
    sentence = models.CharField(max_length=1000 , blank=False, null=False)
    profile = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.sentence
