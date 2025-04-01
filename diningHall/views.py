from django.shortcuts import render, redirect
from .models import Student, MealPlan, Menu
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import check_password
from .forms import LoginForm, AdminLoginForm
import django_tables2 as tables
from django_tables2 import RequestConfig
from django_tables2.paginators import LazyPaginator
from .tables import *

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            password = form.cleaned_data['password']

            user = authenticate(request, username=student_id, password=password)

            if user is not None:
                if user.is_staff:  # Prevent staff users from logging in
                    form.add_error(None, "Invalid credentials")
                else:
                    login(request, user)
                    return redirect('profile')
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def create(request):
    meal_plans = MealPlan.objects.all()
    if request.method == "POST":
        sid = request.POST["student_id"]
        password = request.POST["password"]
        plan = request.POST["plan"]

        # Check if the user with the given student_id exists, if not create a new user
        user, created = User.objects.get_or_create(username=sid, defaults={"is_staff": False})

        if created:
            user.set_password(password)
            user.save()

            # Retrieve the selected meal plan
            meal_plan = MealPlan.objects.get(id=plan)

            # Create the student instance
            student = Student(
                user=user,
                balance=0,  # Default balance
                meal_plan=meal_plan
            )
            student.save()

            return redirect("login")  # Redirect to login page after success
        else:
            return render(request, "registration/create.html", {'meal_plans': meal_plans, "error": "Student ID already in use!"})

    return render(request, "registration/create.html", {'meal_plans': meal_plans})

def admin_login_view(request):
    if request.method == "POST":
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if not user.is_staff:  # Prevent non-staff users from logging in
                    form.add_error(None, "Invalid credentials")
                else:
                    login(request, user)
                    return redirect('admin_dashboard')  # Redirect to admin dashboard
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = AdminLoginForm()

    return render(request, 'administration/login.html', {'form': form})

def admin_dashboard(request):
    table = MenuTable(Menu.objects.all())
    RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(table)
    if request.method == "POST":
        form = MenuCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if not user.is_staff:  # Prevent non-staff users from logging in
                    form.add_error(None, "Invalid credentials")
                else:
                    login(request, user)
                    return redirect('admin_dashboard')  # Redirect to admin dashboard
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = MenuCreateForm()
    return render(request, 'administration/dashboard.html', {'table': table})
