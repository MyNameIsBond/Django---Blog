from django.conf.urls import url
from .views import  (detail      , 
                    create_post , 
                    update_post , 
                    delete_post ,
                    search      ,)
# Post 

urlpatterns = [
    url(r'^(?P<id>\d+)/edit/$', update_post, name = "update"),    
    url(r'^(?P<id>\d+)/detail/$', detail, name="detail"),
    url(r'^(?P<id>\d+)/delete/$', delete_post, name="delete"),
    url(r'^create/$', create_post, name="create"),
    url(r'^search/$', search, name="search"),
]