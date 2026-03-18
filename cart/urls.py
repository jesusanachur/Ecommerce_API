from django.urls import path
from .views import CartViewSet

cart_list = CartViewSet.as_view({'get': 'list', 'post': 'create'})
cart_item_delete = CartViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('', cart_list, name='cart-detail'),
    path('items/<int:pk>/', cart_item_delete, name='cart-item-delete'),
]
