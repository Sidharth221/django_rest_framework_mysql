from rest_framework import serializers

from .models import GroceryProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroceryProduct
        fields = '__all__'