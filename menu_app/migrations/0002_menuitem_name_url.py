# Generated by Django 4.1.4 on 2022-12-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='name_url',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
