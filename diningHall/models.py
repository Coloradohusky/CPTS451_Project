from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.
class MealPlan(models.Model):
    max_balance = models.DecimalField("Max Balance", max_digits = 8, decimal_places = 2)

# class StudentUser(AbstractBaseUser, PermissionsMixin):
#     student_id = models.IntegerField(unique=True)
#     USERNAME_FIELD = "student_id"
#     balance = models.DecimalField("Balance", max_digits=8, decimal_places=2)
#     meal_plan = models.ForeignKey(
#         MealPlan,
#         verbose_name="Meal Plan",
#         on_delete=models.RESTRICT
#     )

#     groups = models.ManyToManyField(
#         Group,
#         related_name="student_users",
#         blank=True
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name="student_users_permissions",
#         blank=True
#     )

#     def save(self, *args, **kwargs):
#         """Ensure password hashing and add user to Students group."""
#         if self.pk is None and self.password:  # Only hash if the user is new
#             self.password = make_password(self.password)

#         super().save(*args, **kwargs)  # Save user first

#         group, created = Group.objects.get_or_create(name="Students")  # Ensure group exists
#         self.groups.add(group)  # Add user to "Students" group

#     def __str__(self):
#         return str(self.student_id)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField("Balance", max_digits=8, decimal_places=2)
    meal_plan = models.ForeignKey(
        MealPlan,
        verbose_name="Meal Plan",
        on_delete=models.RESTRICT
    )

class Menus(models.Model):
    pk = models.CompositePrimaryKey("menu_id", "item_id")
    menu_id = models.PositiveIntegerField("Menu ID")
    item_id = models.CharField("Item Name", max_length = 20)
    info = models.TextField("Nutritional Info")
    cost = models.DecimalField("Cost", max_digits = 6, decimal_places = 2)

class PurchaseHistory(models.Model):
    student = models.ForeignKey(
        Student,
        verbose_name = "Student",
        on_delete = models.CASCADE
    )
    item_id = models.CharField("Item Name", max_length = 20)
    dop = models.DateField("Date of Purchase")
    cost = models.DecimalField("Cost", max_digits = 6, decimal_places = 2)

class Feedback(models.Model):
    response = models.TextField("Response")

class Admin(models.Model):
    password = models.CharField("Password", max_length = 30)

class Report(models.Model):
    item_id = models.CharField("Item Name", max_length = 20, primary_key = True)
    amount = models.PositiveIntegerField("Amount Purchased")