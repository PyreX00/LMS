from django_filters import rest_framework as filters
from .models import Book, Loan

class BookFilter(filters.FilterSet):
    
    class Meta:
        model: Book
        fields = {
            'title':['exact','contains'],
            'author':['exact','contains'],
            'genre':['exact','contains']
        }

class LoanFilter(filters.FilterSet):
    class Meta:
        model = Loan  
        fields = {
            'user__name': ['contains']
        }