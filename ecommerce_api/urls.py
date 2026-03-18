from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_info(request):
	return JsonResponse({
		'message': 'Ecommerce API',
		'version': '1.0.0',
		'endpoints': {
			'admin': '/admin/',
			'accounts': '/api/accounts/',
			'products': '/api/products/',
			'cart': '/api/cart/',
			'orders': '/api/orders/'
		}
	})

urlpatterns = [
	path('', include('frontend.urls')),
	path('api/', api_info, name='api-info'),
	path('admin/', admin.site.urls),
	path('api/accounts/', include('accounts.urls')),
	path('api/products/', include('products.urls')),
	path('api/cart/', include('cart.urls')),
	path('api/orders/', include('orders.urls')),
]

