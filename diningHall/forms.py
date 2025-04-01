from django import forms

class AdminLoginForm(forms.Form):
    username = forms.CharField(label="Admin Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class LoginForm(forms.Form):
    student_id = forms.CharField(label="Student ID", max_length=8)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class MenuCreateForm(forms.Form):
    menu_id = forms.PositiveIntegerField("Menu ID")
    item_id = forms.CharField("Item Name", max_length = 20)
    info = forms.TextField("Nutritional Info")
    cost = forms.DecimalField("Cost", max_digits = 6, decimal_places = 2)