from django.urls import path
from rest_framework import routers
from .views import GenreViewSet,BookViewSet, UserViewSet, LoanViewSet, FineViewSet


router = routers.SimpleRouter()
router.register('Genre', GenreViewSet, basename = "Genre")
router.register('Book',BookViewSet, basename = "book")
router.register('User', UserViewSet, basename = "user")
router.register('Loan', LoanViewSet,basename='loan')
router.register('Fine', FineViewSet, basename='fine')

urlpatterns = [
    
] + router.urls
