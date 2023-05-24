from django.contrib import admin
from .models import *

# Register your models here.

class Blogadmin(admin.ModelAdmin):
    list_display = ['title',"content","author"]

class commentadmin(admin.ModelAdmin):
    list_display = ['content',"author","blog_post"]


admin.site.register(BlogPost,Blogadmin)
admin.site.register(Comment,commentadmin)
