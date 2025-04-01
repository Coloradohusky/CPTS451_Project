from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.
class MealPlan(models.Model):
    max_balance = models.DecimalField("Max Balance", max_digits = 8, decimal_places = 2)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField("Balance", max_digits=8, decimal_places=2)
    meal_plan = models.ForeignKey(
        MealPlan,
        verbose_name="Meal Plan",
        on_delete=models.RESTRICT
    )

class Menu(models.Model):
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

class Report(models.Model):
    item_id = models.CharField("Item Name", max_length = 20, primary_key = True)
    amount = models.PositiveIntegerField("Amount Purchased")