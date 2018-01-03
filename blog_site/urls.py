from django.urls        	 import path,include
from django.contrib          import admin
from django.conf             import settings
from django.conf.urls.static import static
from posts.views             import home

urlpatterns = [

    path('admin/',  admin.site.urls,name="admin"),
    path('home/',			   home,name="base"),
    path('',include('account.urls', namespace="account")),
    path('',include('posts.urls',   namespace="posts")),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)