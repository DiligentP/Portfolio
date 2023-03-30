from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('activity/', views.activity, name='activity'),
    path('skill/', views.skill, name='skill'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
