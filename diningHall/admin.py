from django.contrib import admin

from .models import MealPlan, Student, PurchaseHistory, Feedback, Report

# Register your models here.
admin.site.register(MealPlan)
# admin.site.register(Student)
# admin.site.register(Menus)
admin.site.register(PurchaseHistory)
admin.site.register(Feedback)
# admin.site.register(Admin)
admin.site.register(Report)
admin.site.register(Student)

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('username', 'balance', 'meal_plan')
