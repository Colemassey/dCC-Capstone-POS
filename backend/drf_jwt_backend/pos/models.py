from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Food_id = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    notes = models.CharField(max_length=150)

class Food(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.BigIntegerField()
    topping = models.BooleanField()
    drink = models.BooleanField()
    sides = models.BooleanField()
    size = models.BooleanField()