from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('сlients/', сlients, name='сlients'),
    path('goods/', goods, name='goods'),
    path('employees/', employees, name='employees'),
    path('сlient/<slug:client_slug>/', show_сlient, name='сlient'),
    path('reports/', reports, name='reports'),


]