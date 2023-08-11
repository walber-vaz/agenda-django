from django.db import models
from django.utils import timezone


class Contact(models.Model):
    firt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
