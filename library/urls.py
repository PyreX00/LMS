from django.urls import path
from rest_framework import routers
from .views import GenreViewSet,BookViewSet, UserViewSet, LoanViewSet


router = routers.SimpleRouter()
router.register('Genre', GenreViewSet, basename = "Genre")
router.register('Book',BookViewSet, basename = "book")
router.register('User', UserViewSet, basename = "user")
router.register('Loan', LoanViewSet,basename='loan')

urlpatterns = [
    
] + router.urls
