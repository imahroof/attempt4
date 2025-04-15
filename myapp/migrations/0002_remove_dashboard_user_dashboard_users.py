# Generated by Django 5.1.6 on 2025-04-03 19:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='User',
        ),
        migrations.AddField(
            model_name='dashboard',
            name='Users',
            field=models.ManyToManyField(related_name='dashboards', to=settings.AUTH_USER_MODEL),
        ),
    ]
