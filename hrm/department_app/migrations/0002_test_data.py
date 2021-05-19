# Generated by Django 3.1.7 on 2021-04-07 12:54

from django.db import migrations
from djmoney.money import Money


def forward_func(apps, schema_editor):
    Department = apps.get_model('department_app', 'Department')
    Employee = apps.get_model('department_app', 'Employee')
    User = apps.get_model('department_app', 'User')

    Department.objects.bulk_create([
        Department(name='Executive Office', status='Active'),
        Department(name='The Secretariat', status='Active'),
        Department(name='Accounting', status='Active'),
    ])

    dep_exe = Department.objects.get(name='Executive Office')
    dep_sec = Department.objects.get(name='The Secretariat')
    dep_acc = Department.objects.get(name='Accounting')

    Employee.objects.bulk_create([
        Employee(name='Maria Nankov', department=dep_exe, date='1986-11-01',
                 salary=Money(1500, 'USD'), email='maria@gmail.com', status='Active'),
        Employee(name='Edward Bill', department=dep_sec, date='1966-12-21',
                 salary=Money(1100, 'USD'), email='Edward@gmail.com', status='Active'),
        Employee(name='Pavel Volya', department=dep_acc, date='1985-02-27',
                 salary=Money(2100, 'USD'), email='pavel@gmail.com', status='Active'),
    ])

    User.objects.bulk_create([
        User(username="testuser1", email="testuser1@gmail.com", password="453r5434gdf2"),
        User(username="testuser2", email="testuser2@gmail.com", password="453r5434gdf2"),
        User(username="testuser3", email="testuser3@gmail.com", password="45354r34gdf2"),
    ])


def backward_func(apps, schema_editor):
    Department = apps.get_model('department_app', 'Department')
    Employee = apps.get_model('department_app', 'Employee')
    User = apps.get_model('department_app', 'User')

    Employee.objects.all().delete()
    Department.objects.all().delete()
    User.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('department_app',
         '0001_initial',
         ),
    ]

    operations = [
        migrations.RunPython(forward_func, backward_func),
    ]
