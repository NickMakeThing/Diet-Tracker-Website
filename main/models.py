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
    name = models.CharField(max_length=50,null=True)
    current_weight = models.IntegerField()
    energy = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    carb = models.IntegerField()
    sugars = models.IntegerField()

class WeightChanges(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    weight_change = models.IntegerField()