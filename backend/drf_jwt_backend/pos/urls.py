from django.urls import path, include
from pos import views

urlpatterns = [
    path('customers/', views.get_all_customers),
    path('customers/edit/<int:pk>')
]
