from django.shortcuts import render
from rest_framework import viewsets
from .models import Genre,Book,User,Loan,Fine
from .serializer import GenreSerializer,BookSerializer, UserSerializer,LoanSerializer
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    
