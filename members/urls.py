from re import template
from .views import UserRegisterView,UserEditView,PasswordsChangeView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
      #path('',views.home,name='home'),
      path('register/', UserRegisterView.as_view(),name='register'),
      path('edit_profile/', UserEditView.as_view(),name='edit_profile'),
      path('password/',PasswordsChangeView.as_view(template_name = 'registration/change-password.html')),
      path('password_sucess/',views.password_sucess, name='password_sucess'),
      
      
      
      #path('password/',auth_views.PasswordChangeView.as_view(template_name = 'registration/change-password.html')),
      #django´s admin passwor page
      #path('password/',auth_views.PasswordChangeView.as_view()),
]