from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Router'ı tanımlayın ve ViewSet'i kaydedin
router = DefaultRouter()
# router.register(r'cities', CityViewSet, basename='city')

urlpatterns = [
    path('', include(router.urls)),  # URL'leri router ile yönlendirin
]
