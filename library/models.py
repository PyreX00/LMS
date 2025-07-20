from django.db import models
from datetime import timedelta
from django.utils import timezone
from decimal import Decimal

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=20)
    
    def __str__(self):
        return self.genre
    
class Book(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=30)
    published = models.CharField(max_length=7) 
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    total_book = models.PositiveIntegerField()  
    
    def __str__(self):
        return self.title
    
class User(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=100)  
    
    def __str__(self):
        return self.name

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_date = models.DateField(default=timezone.now, editable=False)
    # returned_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(editable=False)  

    def __str__(self):
        return f"{self.user.name} - {self.book.title}"
    
    def save(self, *args, **kwargs):
        self.due_date = self.loan_date + timedelta(days=15)
        super().save(*args, **kwargs)

class Fine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    returned_date = models.DateField(auto_now_add=True)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    PER_DAY_RATE = Decimal('1.00')  

    def __str__(self):
        return f"Fine for {self.user.name} - ${self.fine_amount}"

    def save(self, *args, **kwargs):
        due_date = self.loan.due_date  # Use due_date instead of loan_date
        today = timezone.now().date()
        days_overdue = (today - due_date).days

        if days_overdue > 0:  # Any days past due date
            self.fine_amount = days_overdue * self.PER_DAY_RATE
        else:
            self.fine_amount = Decimal('0.00')

        super().save(*args, **kwargs)