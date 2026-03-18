from rest_framework import routers
from .views import ProductViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register('', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
