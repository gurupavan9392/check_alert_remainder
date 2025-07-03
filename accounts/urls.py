from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
    path('checkin/', views.check_in, name='checkin'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
