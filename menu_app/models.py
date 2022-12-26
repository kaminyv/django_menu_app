"""
Models for the menu_app
"""
from django.db import models


class Menu(models.Model):
    """
    The model presents a menu
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    The model represents menu items.
    """
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True,
                               null=True)
    name = models.CharField(max_length=50)
    url = models.URLField(blank=True, validators=[])

    def __str__(self):
        return self.name
