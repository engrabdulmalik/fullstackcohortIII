from django.db import models

# Create your models here.
class Drinks(models.Model):
    drink_name=models.CharField(max_length=50)
    drink_type=models.CharField(max_length=50)
    def __str__(self):
        return self.drink_name