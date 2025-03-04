from django import forms
from .models import Expense, Salary

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description']

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['amount']

