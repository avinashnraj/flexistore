from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Uom
from .serializers import UomSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def get_product(request, id):
    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, request.data)
        process_post(serializer)
    elif request.method == 'DELETE':
        product.delete()


def process_post(serializer):
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def process_get(serializer):
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        return process_post(serializer)


@api_view(['GET', 'POST'])
def uoms(request):
    if request.method == 'GET':
        uoms = Uom.objects.all()
        return Response(UomSerializer(uoms, many=True).data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UomSerializer(data=request.data)
        process_post(serializer)
