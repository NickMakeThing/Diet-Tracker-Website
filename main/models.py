from django.db import models
"""
note: all nutritional info is grams per 100g
energy is in kjs
table product
name, unique hash, current weight, energy, proteins, carbs, fats, sugars?

table weight_changes
foreign_key: product, date/time, consumption_amount/weight_change
"""

class Product(models.Model):
    code = models.CharField(max_length=50,null=False,unique=True)
    name = models.CharField(max_length=50,null=True)
    current_weight = models.FloatField()
    energy = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()

class WeightChange(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    date_time = models.CharField(max_length=25) #change to datetime field
    weight_change = models.FloatField()
