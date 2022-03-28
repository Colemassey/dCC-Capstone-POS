from rest_framework import serializers
from .models import Orders, Food, Customer




class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = [ 'id', 'food_id', 'customer_id' 'employee_id', 'type', 'status']

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = [ 'id', 'name', 'price', 'topping', 'drink', 'sides', 'size']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [ 'id', 'first_name', 'last_name', 'address', 'phone_number', 'notes']