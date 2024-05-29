from dataclasses import field, fields
from app.models import Product
from rest_framework import serializers

import product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()    
    class Meta: 
         model = Product
         fields = "__all__"