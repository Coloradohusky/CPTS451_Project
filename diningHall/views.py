from django.shortcuts import render, redirect
from .models import Student, MealPlan, Menu, PurchaseHistory, Report
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, AdminLoginForm, MenuCreateForm, PurchaseHistoryForm
from django_tables2 import RequestConfig
from django_tables2.paginators import LazyPaginator
from .tables import MenuTable, PurchaseHistoryTable, ReportTable
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin, login_url='/accounts/admin_login/')
def admin_dashboard(request):
    menu_table = MenuTable(Menu.objects.all())
    purchase_history_table = PurchaseHistoryTable(PurchaseHistory.objects.all())
    report_table = ReportTable(Report.objects.all())
    RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(menu_table)
    RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(purchase_history_table)
    RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(report_table)

    form = MenuCreateForm()
    pform = PurchaseHistoryForm()

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "menu":
            form = MenuCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("admin_dashboard")

        elif form_type == "purchase":
            pform = PurchaseHistoryForm(request.POST)
            if pform.is_valid():
                pform.save()
                return redirect("admin_dashboard")

    return render(request, "administration/dashboard.html", {"menu_table": menu_table, "purchase_history_table": purchase_history_table, "report_table": report_table, "form": form, "pform": pform})

@login_required
def student_dashboard(request):
    menu_table = MenuTable(Menu.objects.all())
    RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(menu_table)

    return render(request, "student/menuDash.html", {"menu_table": menu_table})

@login_required
def balance_history(request):
    username = request.user
    student = Student.objects.get(user=username)
    balance = student.balance

    return render(request, "student/balanceHistory.html", {"balance": balance})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

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
                    return redirect('student_dashboard')
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
