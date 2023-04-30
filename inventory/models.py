'''
Models for inventory app

Inventory will have different categories
Each category will have different items associated with it
'''
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)


class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=32)
    quantity = models.IntegerField(default=0)
    description = models.TextField()