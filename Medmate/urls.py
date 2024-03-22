"""
URL configuration for Medmate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from base.Views.Auth import *
from base.Views.Notify import *
from django.views.static import serve
from Medmate import settings




urlpatterns = [
    path("admin/", admin.site.urls),
]

NotifyUrls = [
    path('add_notify', add_notification, name='add_notify'),
    path('delete_notify/<uuid:notification_id>', delete_notification, name='delete_notify'),
    path('edit_notify/<uuid:notification_id>', edit_notification, name='edit_notify'),
<<<<<<< HEAD
    path('notification', notification, name='notification'),
=======
>>>>>>> 18e8eaebd863f4b8075c51f80dbf675fada486a4
]

Auth = [
    path('login', login_view, name='login'),
    path('signup', signup_view, name='signup'),
]

admin_ = [
    path('admin/', admin.site.urls),    
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]


urlpatterns.extend(Auth)
urlpatterns.extend(NotifyUrls)
<<<<<<< HEAD
urlpatterns.extend(admin_)

=======
>>>>>>> 18e8eaebd863f4b8075c51f80dbf675fada486a4
