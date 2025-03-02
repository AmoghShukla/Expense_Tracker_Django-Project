from django import forms
from .models import Expense, Salary

class ExpenseForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description', 'date']

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['amount']

