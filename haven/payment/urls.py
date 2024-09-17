from . import views
from django.urls import path

urlpatterns = [
    path('cart/payment', views.index, name='amount.html'),
]