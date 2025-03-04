from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.expense_list, name='expense_list'),
    path('add/', views.add_expense, name='add_expense'),
    path('delete/<int:id>/', views.delete_expense, name='delete_expense'),
    path('analysis/', views.expense_analysis, name='expense_analysis'),
    path('salary/', views.set_salary, name='set_salary'),
]
