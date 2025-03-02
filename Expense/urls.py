from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
    path('analysis/', views.expense_analysis, name='expense_analysis'),  # New route
    path('salary/', views.set_salary, name='set_salary'),

]
