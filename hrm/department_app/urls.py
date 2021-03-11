"""URLS"""

from django.urls import path

from .views import views

urlpatterns = [
    path('',views.main,name='home'),
    path('add_department',views.add_department,name='add_depart'),
    path('manage_department',views.manage_department,name='manage_depart'),
    path('add_employee',views.add_employee,name='employee'),
    path('employees_list',views.employees_list,name='employess_l'),
    path('login_form',views.login_form,name='login'),
    path('change_password',views.change_password,name='change_pass'),
    path('confirm_password',views.confirm_password,name='conf_pass'),
    path('reset_password',views.reset_password,name='reset_pass'),
    path('page_for_user',views.page_for_user,name='user'),
]
