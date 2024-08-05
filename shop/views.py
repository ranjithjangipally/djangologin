from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Order.objects.create(product=product, quantity=1)
    return redirect('product_list')

def checkout(request):
    orders = Order.objects.all()
    total = sum(order.product.price * order.quantity for order in orders)
    return render(request, 'shop/checkout.html', {'orders': orders, 'total': total})
