from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/create/', views.create, name='create'),
    path('accounts/admin_login/', views.admin_login_view, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('balance_history/', views.balance_history, name='balance_history'),
    path('', lambda request: redirect('/accounts/login/', permanent=False)),
]