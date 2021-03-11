"""Django views"""
from django.shortcuts import render


from department_app.models import department,employees


def main(request):
    """main"""
    return render(request,'department_app/main.html')


def add_department(request):
    """add_department"""
    return render(request,'department_app/add_department.html')


def manage_department(request):
    """manage_department"""
    depart = department.Department.objects.order_by('-id')
    return render(request,'department_app/manage_department.html',{'depart':depart})


def add_employee(request):
    """add_employee"""
    return render(request,'department_app/add_employee.html')


def employees_list(request):
    """employees_list"""
    employee = employees.Employees.objects.order_by('-id')
    return render(request,'department_app/employees_list.html',{'employee':employee})


def login_form(request):
    """login_form"""
    return render(request,'department_app/login_form.html')


def change_password(request):
    """change_password"""
    return render(request,'department_app/change_password.html')


def confirm_password(request):
    """confirm_password"""
    return render(request,'department_app/confirm_password.html')


def reset_password(request):
    """reset_password"""
    return render(request,'department_app/reset_password.html')


def page_for_user(request):
    """page_for_user"""
    return render(request,'department_app/page_for_user.html')
