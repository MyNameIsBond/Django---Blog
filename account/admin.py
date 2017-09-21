from django.contrib import admin
from .models import Profile 


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "location" , "email" )
    search_fields = ("user", "location", "email" )





admin.site.register(Profile,UserAdmin)