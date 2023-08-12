from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(
        upload_to='pictures/%Y/%m/', blank=True, null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
