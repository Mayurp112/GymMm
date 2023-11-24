from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from authapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home,name='home'),
    path('signup',signup,name='signup'),
    path('login',loginpage,name='login'),
    path('logout',logoutpage,name='logout'),
    

    

]

