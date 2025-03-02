from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Expense, Category, Salary
from .forms import ExpenseForm
from django.utils import timezone
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.shortcuts import render
from .models import Expense

def generate_pie_chart(expenses):
    category_totals = {}
    
    for expense in expenses:
        category = expense.category.name
        category_totals[category] = category_totals.get(category, 0) + expense.amount

    if not category_totals:
        return None  # No data to show
    
    fig, ax = plt.subplots()
    ax.pie(category_totals.values(), labels=category_totals.keys(), autopct='%1.1f%%', startangle=90, colors=["#FF5733", "#33FF57", "#3357FF", "#F333FF"])
    ax.axis('equal')  

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)
    encoded_chart = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{encoded_chart}"

def expense_analysis(request):
    expenses = Expense.objects.filter(user=request.user)
    total_expense = sum(exp.amount for exp in expenses)
    expense_chart = generate_pie_chart(expenses)

    return render(request, 'Expense/analysis.html', {
        'total_expense': total_expense,
        'expense_chart': expense_chart
    })



def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    total_expense = sum(exp.amount for exp in expenses)
    
    salary_obj, created = Salary.objects.get_or_create(user=request.user)
    money_left = salary_obj.amount - total_expense

    print(f"Total Expenses: {total_expense}")

    return render(request, 'Expense/list.html', {
        'expenses': expenses,
        'salary': salary_obj.amount,
        'money_left': money_left,
        'total_expense': total_expense
    })

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')  # Redirect after saving
    else:
        form = ExpenseForm()

    return render(request, 'Expense/add.html', {'form': form})


def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'Expense/delete.html', {'expense': expense})
