from django.conf.urls        import url, include
from django.contrib          import admin
from django.conf             import settings
from django.conf.urls.static import static
from posts.views             import (home  ,
                                    detail  , 
                                    create_post , 
                                    update_post , 
                                    delete_post ,
                                    search      ,
                                    )
urlpatterns = [
    url(r'^admin/', admin.site.urls, name ="admin"),
    url(r'^$', home, name ="base"),
    url(r'^(?P<id>\d+)/edit/$', update_post, name = "update"),    
    url(r'^(?P<id>\d+)/detail/$', detail, name="detail"),
    url(r'^(?P<id>\d+)/delete/$', delete_post, name="delete"),
    url(r'^create/$', create_post, name="create"),
    url(r'^search/$', search, name="search"),
    url(r'^', include('account.urls',namespace="account")),    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)