from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Customer, Food, Orders
from .serializers import CustomerSerializer, FoodSerializer, OrdersSerializer
from django.contrib.auth.models import User
from rest_framework.request import Request
import http.client
from django.http import JsonResponse

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_customers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        raise Http404
    serializer = CustomerSerializer(customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

