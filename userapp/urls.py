from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.UserRegistration.as_view(), name='signup'),
    path('signin', views.UserLogin.as_view(), name='signin'),
    path('signout', views.logout_user, name='signout')


]
