from django.shortcuts import render
from rest_framework import viewsets,status
from .models import Genre,Book,User,Loan,Fine
from .serializer import GenreSerializer,BookSerializer, UserSerializer,LoanSerializer, FineSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import permissions
from .permission import IsAuthenticatedOrReadOnly,IsSuperUserOrReadOnly
from rest_framework import filters
from .filters import BookFilter, LoanFilter
from django_filters import rest_framework as filter
# Create your views here.

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    
    premission_classes = [IsAuthenticatedOrReadOnly]
    
    def delete(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        book = Book.objects.filter(book__genre=genre).count()  
        if book > 0:
            return Response({"Details": "Genre exists in books, can't delete"})
        genre.delete()
        return Response({"Details": "Genre deleted"}, status=status.HTTP_204_NO_CONTENT)
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = (filters.SearchFilter,filter.DjangoFilterBackend,)
    filter_class = BookFilter
    filterset_fields = ['title', 'author','genre']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    permission_classes = [IsSuperUserOrReadOnly]
    
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    
    permission_classes = [IsSuperUserOrReadOnly]
    filter_backends = (filter.DjangoFilterBackend,)
    filter_class = LoanFilter
    filterset_fields = ['user','due_date']
    
class FineViewSet(viewsets.ModelViewSet):
    queryset = Fine.objects.all()
    serializer_class = FineSerializer
    
    permission_classes = [permissions.IsAuthenticated]


    
