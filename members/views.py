from cProfile import Profile
from dataclasses import field

from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import ProfilePageForm, SignUpForm, EditProfileForm,PasswordChangingForm,ProfilePageForm
from django.views.generic import DetailView,CreateView
from myblog.models import Profile

class CreateProfilePageView(CreateView):
    
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    #fields = ('__all__')

    # choosing the right user by coding not JS
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio','profile_pic','website_url','facebook_url','instagram_url']
    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self,*args,** kwargs):
        
        # get all data in users
        # users =  Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args,** kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

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
    success_url = reverse_lazy('home')

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