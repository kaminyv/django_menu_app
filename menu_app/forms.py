"""
Forms for menu_app.
"""
from django import forms
from .models import MenuItem


class MenuItemAdminForm(forms.ModelForm):
    """
    Form for menu items in the admin panel.
    """

    class Meta:
        model = MenuItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        menu_id = self.initial.get('menu')

        query_items = MenuItem.objects.filter(menu_id=menu_id)
        self.fields['parent'].queryset = query_items
