from django.shortcuts import render
from .models import Customer, Order
# Create your views here.


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'crm_app/customer_list.html', {'customers': customers})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'crm_app/order_list.html', {'orders': orders})