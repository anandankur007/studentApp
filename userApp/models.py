from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)  # `null=False` means this field cannot be empty
    email = models.EmailField()

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email
        }
