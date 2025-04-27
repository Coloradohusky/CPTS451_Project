from django.shortcuts import render, redirect
from .models import Student, MealPlan, Menu, PurchaseHistory, Report, Feedback
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, AdminLoginForm, MenuCreateForm, PurchaseHistoryForm, MenuUpdateForm
from django_tables2 import RequestConfig
from django_tables2.paginators import LazyPaginator
from .tables import MenuTable, PurchaseHistoryTable, ReportTable, FeedbackTable
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin, login_url='/accounts/admin_login/')
def admin_dashboard(request):
    form = MenuCreateForm()
    pform = PurchaseHistoryForm()
    uform = None  # New: update form
    selected_menu = None

    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "menu":
            form = MenuCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_dashboard')
        elif form_type == "purchase":
            pform = PurchaseHistoryForm(request.POST)
            if pform.is_valid():
                pform.save()
                return redirect('admin_dashboard')
        elif form_type == "update_menu":
            menu_value = request.POST.get('menu_item')
            menu_id, item_id = menu_value.split("|")
            selected_menu = Menu.objects.get(pk=(menu_id, item_id))
            if 'delete' in request.POST:
                selected_menu.delete()
                return redirect('admin_dashboard')
            else:
                uform = MenuUpdateForm(request.POST, instance=selected_menu)
                if uform.is_valid():
                    uform.save()
                    return redirect('admin_dashboard')

    else:
        uform = MenuUpdateForm()

    menu_items = Menu.objects.all()

    return render(request, "administration/dashboard.html", {
        "form": form,
        "pform": pform,
        "uform": uform,
        "menu_items": menu_items,
        "selected_menu": selected_menu,
    })


@login_required
def student_dashboard(request):
    menu_table = MenuTable(Menu.objects.all())
    RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(menu_table)

    return render(request, "student/menuDash.html", {"menu_table": menu_table})

@login_required
def balance_history(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    username = request.user
    studentid = Student.objects.get(user=username)
    balance = studentid.balance

    purchase_history_table = PurchaseHistoryTable(PurchaseHistory.objects.filter(student = studentid))
    RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(purchase_history_table)

    return render(request, "student/balanceHistory.html", {"balance": balance, "purchase_history_table": purchase_history_table})

@login_required
def feedback(request):
    if request.method == "POST":
        service = request.POST["choice"]
        name = request.POST["name"]
        rating = request.POST["rate"]
        desc = request.POST["description"]

        feedback = "Service: " + service + ", Name: " + name + ", Rating: " + rating + ", Desc: " + desc

        Feedback.objects.create(response = feedback)

        return redirect("student_dashboard")

    return render(request, "student/feedback.html")

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

def admin_menu_table(request):
    menu_table = MenuTable(Menu.objects.all())
    RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(menu_table)
    return render(request, 'administration/menu_table.html', {"menu_table": menu_table})

def admin_purchase_history(request):
    purchase_history_table = PurchaseHistoryTable(PurchaseHistory.objects.all())
    RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(purchase_history_table)
    return render(request, 'administration/purchase_history.html', {"purchase_history_table": purchase_history_table})

def admin_report_table(request):
    report_table = ReportTable(Report.objects.all())
    RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(report_table)
    return render(request, 'administration/report_table.html', {"report_table": report_table})

def admin_feedback(request):
    feedback_table = FeedbackTable(Feedback.objects.all())
    RequestConfig(request, paginate={"per_page": 20, "paginator_class": LazyPaginator}).configure(feedback_table)
    return render(request, 'administration/feedback_table.html', {"feedback_table": feedback_table})
