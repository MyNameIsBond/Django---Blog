from django.contrib import admin
from .models import Posts 

class PostsAdmin(admin.ModelAdmin):
    list_display = ("pub_date", "title" )






admin.site.register(Posts,PostsAdmin)