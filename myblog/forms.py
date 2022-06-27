from logging import PlaceHolder
from secrets import choice
from django import forms
from .models import Post,Category,Comment
from django.forms import ModelForm

#python list with select boxes....igual tuples args..static way...
#options =[('coding','coding'),('sports','sports'),('entertainment','entertainment'),]
#getting options from a querySET in python
choices = Category.objects.all().values_list('name','name')
#looping to get a python list in choice_list
choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','author','category','body','snippet','header_image')
        #bootstrapify....styling....others attrs in the python dict...
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}), 
            #'author':forms.TextInput(attrs={'class':'form-control','placeholder':'user name','id':'elder'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            #'author':forms.Select(attrs={'class':'form-control'}), 
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),  
          
                    }
#create a Venue form from a class and Meta allows to defines class?
'''class VenueForm( ModelForm):
    class Meta:
        model = Venue
        fields = ('name','address','zip_code','phone','web','email_address')'''

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body','snippet')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'This is a placeholder on Title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}), 
            #'author':forms.Select(attrs={'class':'form-control'}), 
            'body':forms.Textarea(attrs={'class':'form-control'}), 
            'snippet':forms.Textarea(attrs={'class':'form-control'}), 
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'body':forms.Textarea(attrs={'class':'form-control'}), 
            
        }