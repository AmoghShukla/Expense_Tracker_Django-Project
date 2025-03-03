from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Category, Salary
from .forms import ExpenseForm, SalaryForm
from django.utils import timezone
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Function to generate a pie chart for expense categories
def generate_pie_chart(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense.category.name
        category_totals[category] = category_totals.get(category, 0) + expense.amount

    if not category_totals:
        return None  # No data to display

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

# View for detailed expense analysis
def expense_analysis(request):
    expenses = Expense.objects.all()
    total_expense = sum(exp.amount for exp in expenses)
    expense_chart = generate_pie_chart(expenses)

    return render(request, 'Expense/analysis.html', {
        'total_expense': total_expense,
        'expense_chart': expense_chart
    })

# View to list all expenses
def expense_list(request):
    expenses = Expense.objects.all()
    total_expense = sum(exp.amount for exp in expenses)
    
    salary_obj, created = Salary.objects.get_or_create(defaults={'amount': 0})
    money_left = salary_obj.amount - total_expense

    return render(request, 'Expense/list.html', {
        'expenses': expenses,
        'salary': salary_obj.amount,
        'money_left': money_left,
        'total_expense': total_expense
    })

# View to add a new expense with date selection
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()

    return render(request, 'Expense/add.html', {'form': form})

# View to delete an expense
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'Expense/delete.html', {'expense': expense})

# View to set or update the monthly salary
def set_salary(request):
    salary, created = Salary.objects.get_or_create(id=1, defaults={'amount': 0})

    if request.method == "POST":
        form = SalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = SalaryForm(instance=salary)

    return render(request, 'Expense/salary.html', {'form': form})