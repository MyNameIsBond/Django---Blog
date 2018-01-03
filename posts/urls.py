from django.urls 	  import path , include
from .views 		  import  *


app_name="posts"

urlpatterns = [

    path('edit/<slug>',  update_post, name="update"),    
    path('detail/<slug>',detail, 	  name="detail"),
    path('delete/<slug>',delete_post, name="delete"),
    path('create/', 	 create_post, name="create"),
    path('search/', 	 search, 	  name="search"),

]