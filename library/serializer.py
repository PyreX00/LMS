from rest_framework import serializers
from .models import Genre,Book, User, Loan, Fine

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = "__all__"
    
    def create(self, validated_data):
        total_number = self.Meta.model.objects.filter(genre = validated_data.get('genre')).count()
        if total_number > 0 :
            raise serializers.ValidationError("Genre already exists")
        genre = self.Meta.model(**validated_data)
        genre.save()
        return genre
    
class BookSerializer(serializers.ModelSerializer):
    
    genre = serializers.StringRelatedField()
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset = Genre.objects.all(),
        source = 'genre'
    )
    
    class Meta:
        model = Book 
        fields = ['id','title','author','published','total_book','genre_id','genre']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields  = "__all__"
        
class LoanSerializer(serializers.ModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    
    class Meta:
        model = Loan
        fields = ['id', 'book', 'user', 'loan_date', 'due_date']
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        data['book_title'] = str(instance.book)  
        data['user_name'] = str(instance.user)   
        return data
    
class FineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fine
        fields = "__all__"
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        data['user_name'] = str(instance.user)
        data['book_title'] = str(instance.loan.book)
        data['loan_date'] = instance.loan.loan_date
        data['expected_return_date'] = instance.loan.due_date
        data['actual_return_date'] = instance.returned_date
        data['days_overdue'] = max(0, (instance.returned_date - instance.loan.due_date).days)
        data['per_day_rate'] = str(instance.PER_DAY_RATE)
        return data