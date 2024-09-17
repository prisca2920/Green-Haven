from django.db.models import Sum
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required


def product_list(request):
    products = Product.objects.all()

    cart_count = CartItem.objects.filter(user=request.user).aggregate(Sum('quantity'))['quantity__sum']
    cart_count = cart_count if cart_count else 0
    price = 0
    return render(request, 'index.html', {'products': products, 'cart_count': cart_count, 'price': price})


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
        cart_item.quantity += 1
        cart_item.save()

        return redirect('cart:product_list')
    else:
        return HttpResponse('You must be logged in to add items to the cart.')


def reset_cart(request):
    user_cart_items = CartItem.objects.filter(user=request.user)
    user_cart_items.delete()
    return HttpResponseRedirect('/cart/')


def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('cart:view_cart')


def details(request):
    return render(request, 'detail.html')


def contact(request):
    return render(request, 'contact.html')

def faq_view(request):
    return render(request, 'faq.html')


def cart(request):
    return render(request, 'cart.html')


def cart_count(request):
    cart_count = CartItem.objects.filter(user=request.user).aggregate(Sum('quantity'))['quantity__sum']
    cart_count = cart_count if cart_count else 0
    return JsonResponse({'cart_count': cart_count})

