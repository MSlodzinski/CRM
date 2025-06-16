# crm_app/urls.py
from django.urls import path
from django.http import HttpResponse
from . import views

def index(request):
    return HttpResponse("Witaj w CRM!")

def main_page(request):
    return HttpResponse("To jest strona główna CRM.")

urlpatterns = [
    path('', view=main_page, name='main_page'), # TODO: Implement main_page view
    # path('/customers', view=customer_list, name='customer_list'),
]