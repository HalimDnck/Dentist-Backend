from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)

router = DefaultRouter()
router.register('', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),  
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
