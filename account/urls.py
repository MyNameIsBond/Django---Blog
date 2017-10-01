from django.conf.urls    import url , include
from .views              import *
from django.contrib.auth import views as auth_views
# account 
urlpatterns = [
    
    url(r'^profile/$', profile, name="profile"),
    url(r'^profile/log_in$', log_in, name="log_in"),
    url(r'^profile/log_out$', log_out, name="log_out"),
    url(r'^profile/register$', register, name="register"),
    url(r'^profile/edit$', edit_profile, name="edit"),
    url(r'^profile/edit-password$', edit_password, name="edit-password"),
    url(r'^profile/', include('django.contrib.auth.urls')),

]