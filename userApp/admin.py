from django.contrib import admin
from .models import User  # Import your model

# Register your model with the admin site
admin.site.register(User)
