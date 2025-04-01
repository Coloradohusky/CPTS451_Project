from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('create/', views.create, name='create'),
    path('admin_login/', views.admin_login_view, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard')
]