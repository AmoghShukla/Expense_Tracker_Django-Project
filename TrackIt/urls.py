from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Expense/', include('Expense.urls')),  # Ensure 'Expense/' matches your app URL pattern
    path('accounts/login/', include('django.contrib.auth.urls')),
    
    # Redirect root URL to Expense List
    path('', lambda request: redirect('expense_list', permanent=True)),
]
