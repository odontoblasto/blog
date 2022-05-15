from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post
from .forms import PostForm


# Create your views here.

#def home(request):
#   return render(request, 'home.html',{}) #create from def

class HomeView(ListView):#create from a class
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'author_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields ='__all__'
    #fields = ('title','title_tag','body')#python list of attributes





