from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Order(models.Model):
    STATUSES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUSES, default='pending')
    deadline = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.customer.first_name} {self.customer.last_name} - {self.status}"