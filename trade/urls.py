from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('сlients/', сlients, name='сlients'),
    path('goods/', goods, name='goods'),
    path('employees/', employees, name='employees'),
    path('сlient/<slug:client_slug>/', show_сlient, name='сlient'),
    path('reports_salary/', reports_salary, name='reports_salary'),
    path('reports_salary_manage/', reports_salary_manage, name='reports_salary_manage'),
    path('notes/', notes, name='notes'),


]