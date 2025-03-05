from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Expense, Category, Salary
from .forms import ExpenseForm, SalaryForm
from django.utils import timezone
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO


def logout_view(request):
    if request.method == "POST":  
        logout(request)
        return redirect('signup')  
    return redirect('expense_list')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('expense_list')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


def generate_pie_chart(expenses):
    category_totals = {}

    for expense in expenses:
        
        if isinstance(expense.category, Category):
            category = expense.category.name
        elif isinstance(expense.category, str):
            category = expense.category
        else:
            category = "Uncategorized"  

        category_totals[category] = category_totals.get(category, 0) + expense.amount

    if not category_totals:
        return None  

    fig, ax = plt.subplots()
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#57FFF3", "#FFC300"]

    ax.pie(category_totals.values(), labels=category_totals.keys(), autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  # Equal aspect ratio for a perfect circle

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)
    encoded_chart = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return f"data:image/png;base64,{encoded_chart}"




@login_required
def expense_analysis(request):
    expenses = Expense.objects.filter(user=request.user)  # Fetch only logged-in user's expenses
    total_expense = sum(exp.amount for exp in expenses)
    expense_chart = generate_pie_chart(expenses)

    return render(request, 'Expense/analysis.html', {
        'total_expense': total_expense,
        'expense_chart': expense_chart
    })
@login_required
# View to list all expenses
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    total_expense = sum(exp.amount for exp in expenses)
    
    salary_obj, created = Salary.objects.get_or_create(user=request.user, defaults={'amount': 0})
    money_left = salary_obj.amount - total_expense

    return render(request, 'Expense/list.html', {
        'expenses': expenses,
        'salary': salary_obj.amount,
        'money_left': money_left,
        'total_expense': total_expense
    })


@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    return render(request, 'Expense/add.html', {'form': form})


def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'Expense/delete.html', {'expense': expense})


@login_required
def set_salary(request):
    salary, created = Salary.objects.get_or_create(user=request.user, defaults={'amount': 0})

    if request.method == "POST":
        form = SalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = SalaryForm(instance=salary)

    return render(request, 'Expense/salary.html', {'form': form})
