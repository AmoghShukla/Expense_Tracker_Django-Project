from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Salary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} - ${self.amount}"

class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    category = models.CharField(max_length=255, default="0")
    title = models.CharField(max_length=200, default="Untitled Expense")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.amount} ({self.user.username if self.user else 'No User'})"
