from django.conf.urls        import url, include
from django.contrib          import admin
from django.conf             import settings
from django.conf.urls.static import static
from posts.views             import home

urlpatterns = [
    url(r'^admin/', admin.site.urls, name ="admin"),
    url(r'^$', home, name ="base"),
    url(r'^', include('account.urls',namespace="account")),    
    url(r'^', include('posts.urls',namespace="posts")),    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)