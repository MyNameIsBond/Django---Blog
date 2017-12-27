from django.urls         import path,include
from .views              import *
from django.contrib.auth import views as auth_views
app_name="account" 
urlpatterns = [
  
    path('profile/', 		profile, name="profile"),
    path('profile/log_in', log_in, name="log_in"),
    path('profile/log_out', log_out, name="log_out"),
    path('profile/register',register, name="register"),
    path('profile/edit', 	edit_profile, name="edit"),
    path('profile/edit-password', edit_password, name="edit-password"),
    path('profile/', include('django.contrib.auth.urls')),

]