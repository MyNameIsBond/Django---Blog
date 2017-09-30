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
    # url(r'^profile/password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^profile/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^profile/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^profile/reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),    # url(r'^profile/password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^profile/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^profile/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^profile/reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),    # url(r'^profile/password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^profile/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^profile/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^profile/reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),    # url(r'^profile/password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^profile/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^profile/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^profile/reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),    # url(r'^profile/password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^profile/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    # url(r'^profile/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^profile/reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),