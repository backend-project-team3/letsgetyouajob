from django.db import models
from apps.accounts.models import User
# Create your models here.

class Saved_Job(models.Model):
    username = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    job_id = models.CharField(max_length=50)
    applied = models.BooleanField(default=False)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField()


def __str__(self):
        return self.username + ' said ' + self.text
