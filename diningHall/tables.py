from .models import Menu, PurchaseHistory, Report

import django_tables2 as tables

class MenuTable(tables.Table):
    class Meta:
        model = Menu
        fields = (
            "menu_id", "item_id", "info", "cost"
        )
        template_name = "django_tables2/semantic.html"

class PurchaseHistoryTable(tables.Table):
    class Meta:
        model = PurchaseHistory
        fields = (
            "student__user__username", "item_id", "dop", "cost"
        )
        template_name = "django_tables2/semantic.html"

class ReportTable(tables.Table):
    class Meta:
        model = Report
        fields = (
            "item_id", "amount"
        )
        template_name = "django_tables2/semantic.html"