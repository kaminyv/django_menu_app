"""
Settings for elements of the menu_app admin panel.
"""
from django.contrib import admin
from .forms import MenuItemAdminForm
from .models import Menu, MenuItem


class MenuItemAdminInline(admin.StackedInline):
    """
    Inline form for menu items.
    """
    model = MenuItem
    form = MenuItemAdminForm
    extra = 0


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Menu presentation form in the admin panel.
    """
    inlines = [
        MenuItemAdminInline,
    ]
