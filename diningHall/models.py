from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class MealPlan(models.Model):
    class Meta:
        verbose_name = "Meal Plan"
        verbose_name_plural = "Meal Plans"
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
    def __str__(self):
        return f"{self.item_id} (Menu {self.menu_id})"

class PurchaseHistory(models.Model):
    class Meta:
        verbose_name = "Purchase History"
        verbose_name_plural = "Purchase Histories"
    student = models.ForeignKey(
        Student,
        verbose_name = "Student",
        on_delete = models.CASCADE
    )
    item_id = models.CharField("Item Name", max_length = 20)
    dop = models.DateField("Date of Purchase")
    cost = models.DecimalField("Cost", max_digits = 6, decimal_places = 2)
    def save(self, *args, **kwargs):
        """Override save method to update or create a Report entry when a purchase is made."""
        super().save(*args, **kwargs)  # Save the purchase first
        self.student.balance -= self.cost
        self.student.save()
        report, created = Report.objects.get_or_create(item_id=self.item_id, defaults={"amount": 0})
        report.amount += 1  # Increment the purchase count
        report.save()

class Feedback(models.Model):
    class Meta:
        verbose_name_plural = "Feedback"
    response = models.TextField("Response")

class Report(models.Model):
    item_id = models.CharField("Item Name", max_length = 20, primary_key = True)
    amount = models.PositiveIntegerField("Amount Purchased")
