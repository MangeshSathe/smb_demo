from django.shortcuts import render
import requests
from .models import *

from rest_framework import viewsets,permissions, serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import logging

from .serializers import *
# Create your views here.

logging.basicConfig(level=logging.INFO)

def book_table(request):
    book_data = Book.objects.all()

    return render(request,'book_table.html', {'books': book_data})

serializer_class = BookSerializers
 
@api_view(['GET'])
def book_list(request):
    key = request.headers.get('X-API-KEY')
    if key in ['123456789_POSTMAN','123456789_UI']:
        queryset = Book.objects.all()
        serializer = serializer_class(queryset, many = True)
        return Response(serializer.data)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def book_create(request):
    serializer =  serializer_class(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def book_delete(request,pk):
    try:
        book_found = Book.objects.get(pk = pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    book_found.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def book_edit(request, pk):
    try:
        book_found = Book.objects.get(pk = pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = serializer_class(book_found, data = request.data)
    
    if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)