from django.db import models

# Create your models here.
class Drinks(models.Model):
    drink_name=models.CharField(max_length=50)
    drink_type=models.CharField(max_length=50)
    category_id=models.ForeignKey('DrinksCategory', on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.drink_name

class DrinksCategory(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_name=models.CharField(max_length=50)
    def __str__(self):
        return self.category_name