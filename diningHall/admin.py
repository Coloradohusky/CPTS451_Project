from django.contrib import admin

from .models import MealPlan, Student, PurchaseHistory, Feedback, Report, Menu

# Register your models here.
admin.site.register(MealPlan)
# admin.site.register(Student)
# admin.site.register(Menu)
admin.site.register(PurchaseHistory)
admin.site.register(Feedback)
# admin.site.register(Admin)
admin.site.register(Report)
admin.site.register(Student)

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('username', 'balance', 'meal_plan')
