from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    url(r'^account/',include("accounts.urls") ),
]

urlpatterns += staticfiles_urlpatterns()