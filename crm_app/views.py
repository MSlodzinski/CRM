from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Order
from .forms import CustomerForm, OrderForm

# Create your views here.


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'crm_app/customer_list.html', {'customers': customers})

def add_customer(request):
    if request.mehod == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'crm_app/customer_form.html', {'form': form})

def remove_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'crm_app/remove_customer.html', {'customer': customer})

def edit_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'crm_app/customer_form.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'crm_app/order_list.html', {'orders': orders})