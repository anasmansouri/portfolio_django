from django.db import models
import uuid

# Create your models here.

class OfferedService(models.Model):
    id = models.UUIDField(primary_key=True,uuid=uuid.uuid4,editable=False,unique=True)
    service_name = models.CharField(max_length=200,blank=False,null=False)
    # profile_image = models.ImageField(blank=True, null=True, upload_to='profiles/', default='profiles/user-default.png')

