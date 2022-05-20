from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Category, Post
from .forms import PostForm,EditForm


# Create your views here.
#def home(request):
#   return render(request, 'home.html',{}) #create from def

def CategoryView(request,cats):
    category_post = Post.objects.filter(category = cats)

    return render(request,'categories.html',{'cats':cats.title(),'category_post':category_post})

class HomeView(ListView):#create from a class
    model = Post
    template_name = 'home.html'
    ordering =['-post_date']
    #ordering = ['-id']#inverse post order

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'author_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields ='__all__'
    #fields = ('title','title_tag','body')#python list of attributes


class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



