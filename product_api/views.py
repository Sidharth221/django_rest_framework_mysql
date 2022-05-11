from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import GroceryProduct

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls= {
        'List':'/Grocery-list/',
        'Detail View':'/product-detail/<int:id>/',
        'Create':'/product-create/',
        'Update':'/product-update/<int:id>/',
        'Delete':'/product-detail/<int:id>/',
    }
     
    return Response(api_urls); 

@api_view(['GET'])
def GroceryProducts(request):
    products= GroceryProduct.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def SingleProduct(request, pk):
    product= GroceryProduct.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    
    return Response(serializer.data)


@api_view(['POST'])
def CreateProduct(request):
    
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def updateProduct(request, pk):
    product= GroceryProduct.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 


@api_view(['GET'])
def deleteProduct(request, pk):
    product= GroceryProduct.objects.get(id=pk)
    product.delete()

    return Response("Items delete successfully!")       

