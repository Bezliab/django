from rest_framework import serializers
from productapi.models import ProductAPI

class ProductAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAPI
        fields = ['id', 'name', 'description', 'price', 'date_added']