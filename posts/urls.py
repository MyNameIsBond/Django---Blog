from django.urls 	  import path , include
from .views 		  import  *


app_name="posts"

urlpatterns = [
    path('<int:id>/edit/', 	update_post, 	name="update"),    
    path('<int:id>/detail/', 	detail, 		name="detail"),
    path('<int:id>/delete/', 	delete_post, 	name="delete"),
    path('create/', 				create_post, 	name="create"),
    path('search/', 				search, 		name="search"),

]
    # url(r'^articles/(?P<year>[0-9]{4})/$', 	views.year_archive),
	# path('articles/<int:year>/', 			views.year_archive),