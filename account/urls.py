from django.conf.urls import url
from .views import log_in,log_out,register,profile



# account 
urlpatterns = [
    url(r'^profile/$', profile, name="profile"),
    url(r'^profile/log_in$', log_in, name="log_in"),
    url(r'^profile/log_out$', log_out, name="log_out"),
    url(r'^profile/register$', register, name="register"),
]