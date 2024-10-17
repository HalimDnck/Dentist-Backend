from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.contrib import admin

# Router'ı tanımlayın ve ViewSet'i kaydedin
router = DefaultRouter()
# router.register(r'cities', CityViewSet, basename='city')

urlpatterns = []
