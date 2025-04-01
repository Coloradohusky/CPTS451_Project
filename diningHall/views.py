from django.shortcuts import render, redirect
from .models import Student, MealPlan
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# from django.contrib.auth.hashers import check_password
# from .forms import LoginForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            password = form.cleaned_data['password']

            # Authenticate user based on student_id
            user = authenticate(request, username=student_id, password=password)

            if user is not None:
                login(request, user)
                student = user.student  # Access the Student model linked to the User

                # Example: You can access the student's balance and meal plan
                balance = student.balance
                meal_plan = student.meal_plan

                # Redirect to the dashboard or any other page
                return redirect('profile')  # Replace 'home' with your desired redirect URL
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def create(request):
    if request.method == "POST":
        sid = request.POST["student_id"]
        password = request.POST["password"]
        plan = request.POST["plan"]

        # Check if the user with the given student_id exists, if not create a new user
        user, created = User.objects.get_or_create(username=sid)

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

    return render(request, "registration/create.html")
