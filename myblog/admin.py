from django.contrib import admin
from .models import Post, Category,Profile,Comment
#from .models import Venue
#from .models import MyClubUser
#from .models import Event
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)


