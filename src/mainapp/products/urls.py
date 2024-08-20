from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path(url name, name of the method being called, name=nickname)
    path('admin_console', views.admin_console, name='admin_console'),
    path('<int:pk>/details/', views.details, name='details'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('delete_confirmation/', views.confirmed_delete, name='confirmed'),
    path('new_food/', views.create_item, name='createFood'),
]
