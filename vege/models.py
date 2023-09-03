from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Opportunity(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipe')
    description = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)
    op_link = models.CharField(max_length=300, null=True, blank=True)
    status = models.BooleanField(default=False, null=True, blank=True)
    batch = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=150, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name