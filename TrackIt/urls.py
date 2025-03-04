from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Expense/', include('Expense.urls')),  # Ensure 'Expense' app's URLs are included
    path('accounts/', include('django.contrib.auth.urls')),  # ✅ Add this line

    # Redirect root URL to Expense List
    path('', lambda request: redirect('expense_list', permanent=True)),
]