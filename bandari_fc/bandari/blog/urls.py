from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('checkout/', views.checkout, name='checkout'),
	path('ticket/', views.ticket, name='ticket'),
	path('cart/', views.cart, name='cart'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
