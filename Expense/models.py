from django.db import models
from django.utils import timezone

class Salary(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username} - ${self.amount}"

class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Expense(models.Model):
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.category} - {self.amount}"