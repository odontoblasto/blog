from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
#editing django´s native forms
#bootstrapify with  widgets directly in the form,new fields
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
#botstrapify when the fields are already created by django.auth,old fields
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'