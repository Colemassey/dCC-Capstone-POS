from django.contrib import admin
from .models import Orders, Food, Customer

# Register your models here.

admin.site.register(Orders)
admin.site.register(Food)
admin.site.register(Customer)