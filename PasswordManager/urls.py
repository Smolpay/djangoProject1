from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('user_create', views.user_create, name='user_create'),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('login', views.login_required(), name='login'),
    path('error404', views.error404),



]



