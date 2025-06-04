from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Book)  # Assuming you have a Book model in models.py