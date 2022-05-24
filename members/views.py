from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm,PasswordChangingForm


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    #form_class = PasswordChangeForm
    success_url = reverse_lazy('password_sucess')
    #success_url = reverse_lazy('home')

def password_sucess(request):
    return render(request,'registration/password_sucess.html',{})


class UserRegisterView(generic.CreateView):
    #editing django´s native forms,
    #adding as SignUpForm ,just created in members/forms.py
    
    form_class = SignUpForm 
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    
    # native form from django-UserChangeForm
    # form_class = UserChangeForm
    
    # form updated and customized
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

#  how to get data from the fields
    def get_object(self):
        return self.request.user