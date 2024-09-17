from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'cart'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart_count/', views.cart_count, name='cart_count'),
    path('details/', views.details, name='details'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('faq/', views.faq_view, name='faq'),
    path('admin/', admin.site.urls),
    path('googlelogin/', include('googlelogin.urls')),
]