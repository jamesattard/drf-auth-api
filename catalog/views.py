from .permissions import IsAdminOrReadOnly
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

from rest_framework.views import APIView

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )

class PublicData(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer    

class ProtectedData(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
