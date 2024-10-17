from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)  # `null=False` means this field cannot be empty
    email = models.EmailField()