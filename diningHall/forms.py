from django import forms
from .models import Menu, PurchaseHistory, Student

class AdminLoginForm(forms.Form):
    username = forms.CharField(label="Admin Username", max_length=150)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class LoginForm(forms.Form):
    student_id = forms.CharField(label="Student ID", max_length=8)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class MenuCreateForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["menu_id", "item_id", "info", "cost"]
        labels = {
            "menu_id": "Menu ID",
            "item_id": "Item Name",
            "info": "Nutritional Info",
            "cost": "Cost",
        }

class PurchaseHistoryForm(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=Student.objects.select_related("user").all(),
        label="Username",
        widget=forms.Select,
    )
    class Meta:
        model = PurchaseHistory
        fields = ["student", "item_id", "dop", "cost"]
        labels = {
            "student": "Username",
            "item_id": "Item Name",
            "dop": "Date of Purchase",
            "cost": "Cost",
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["student"].queryset = Student.objects.select_related("user").all()
        self.fields["student"].label_from_instance = lambda obj: obj.user.username

