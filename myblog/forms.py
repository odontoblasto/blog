from logging import PlaceHolder
from django import forms
from .models import Post
from django.forms import ModelForm



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','body')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is a placeholder on Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}), 
            'author':forms.Select(attrs={'class':'form-control'}), 
            'body':forms.Textarea(attrs={'class':'form-control'}), 
          
        }#bootstrapify....styling....others attrs in the python dict...
#create a Venue form from a class and Meta allows to defines class?
'''class VenueForm( ModelForm):
    class Meta:
        model = Venue
        fields = ('name','address','zip_code','phone','web','email_address')'''



class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is a placeholder on Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}), 
            #'author':forms.Select(attrs={'class':'form-control'}), 
            'body':forms.Textarea(attrs={'class':'form-control'}), 
          
        }