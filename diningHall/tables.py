from .models import *

import django_tables2 as tables

class MenuTable(tables.Table):
    pk = tables.Column(linkify=True)

    class Meta:
        model = Menu
        fields = (
            "menu_id", "item_id", "info", "cost"
        )
        template_name = "django_tables2/semantic.html"