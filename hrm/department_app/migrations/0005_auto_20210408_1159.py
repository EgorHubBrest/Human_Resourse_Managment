# Generated by Django 3.1.7 on 2021-04-08 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department_app', '0004_auto_20210407_1351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='status_departmnet',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='status_employee',
            new_name='status',
        ),
    ]
