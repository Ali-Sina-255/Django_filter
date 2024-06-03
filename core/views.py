from django.shortcuts import render

from core.serializers import BooKModelSerializers
from . models import Book

from .filter import BookFilters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view

# Create your views here.
def index_view(request):
    book_filters = BookFilters(request.GET,queryset=Book.objects.all())
    # form = BookNameFilterForm()
    form = book_filters.form
    context = {
        "form":form,
        "books":book_filters.qs
    }
    return render(request, 'index.html',context)


class BookAPIView(APIView):
    
    def get(self, request):
        book = Book.objects.all()
        serializer = BooKModelSerializers(book, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BooKModelSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

