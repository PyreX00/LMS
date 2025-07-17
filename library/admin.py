from django.contrib import admin
from .models import Book, User, Loan, Fine

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','published','genre','total_book']
    search_fields = ['title', 'author', 'genre__genre']
    list_filter = ['genre']
    
admin.site.register(Book, BookAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','address']
    search_fields = ['name','email']
    

admin.site.register(User, UserAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display = ['id','book','user', 'loan_date','due_date',]
    search_fields = ['book', 'user']
    list_filter = ['user','due_date']
    # list_editable = ['returned_date']
    
    
admin.site.register(Loan, LoanAdmin)

class FineAdmin(admin.ModelAdmin):
    list_display = ['id','user','loan','returned_date','fine_amount']

admin.site.register(Fine,FineAdmin)