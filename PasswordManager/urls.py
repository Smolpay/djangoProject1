from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import include



urlpatterns = [
    path('', views.index, name='index'),
    path('user_create', views.user_create, name='user_create'),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('login', views.login_required()),



]



