from django.db import models
import uuid

# Create your models here.

class Items(models.Model):
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=50) 
    quantity = models.IntegerField() 
    rate = models.DecimalField(max_digits=11,decimal_places=2)
    total_cost = models.DecimalField(max_digits=11,decimal_places=2)
