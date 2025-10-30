from django.shortcuts import render
from rest_framework import generics
from productapi.models import ProductAPI
from productapi.serializers import ProductAPISerializer

# Create your views here.
class ProductAPIListCreateView(generics.ListCreateAPIView):
  queryset = ProductAPI.objects.all()
  serializer_class = ProductAPISerializer
