from django.db import models
import uuid


# Create your models here.
class Project(models.Model):
    id = models.UUIDField(primary_key=True, blank=False, null=False, uuid=uuid.uuid4)
    project_name = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=600, blank=False, null=False)
    source_link = models.CharField(max_length=200, blank=True, null=True)
    demonstration_video_link = models.CharField(max_length=200, blank=True, null=True)


class ProgrammingLanguage(models.Model):
    name = models.CharField(primary_key=True, max_length=200, null=False, blank=False)


class Technologie(models.Model):
    name = models.CharField(primary_key=True, max_length=200, null=False, blank=False)
    description = models.CharField(max_length=600, null=True, blank=True)
