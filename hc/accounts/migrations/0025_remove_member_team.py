# Generated by Django 2.1.5 on 2019-01-22 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20190119_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='team',
        ),
    ]