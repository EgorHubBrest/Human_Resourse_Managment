# Generated by Django 3.1.7 on 2021-04-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department_app', '0002_test_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(choices=[('Inactive', 'Inactive'), ('Active', 'Active')], default='Inactive', max_length=8),
        ),
    ]