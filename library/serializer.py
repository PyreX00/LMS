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
    book = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Loan
        fields = ['id', 'loan_date', 'returned_date', 'book', 'user']
        
        