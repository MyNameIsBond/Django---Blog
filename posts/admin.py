from django.contrib import admin
from .models import Posts 
from django.contrib.auth.models import User




class PostsAdmin(admin.ModelAdmin):
    list_display = ("pub_date", "title" )





admin.site.register(Posts,PostsAdmin)
