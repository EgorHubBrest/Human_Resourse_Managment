# Generated by Django 3.2 on 2021-05-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department_app', '0002_test_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]