"""hellodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from  . import  views,search,testdb
from django.conf.urls import url

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


urlpatterns = [
    url(r'^$', views.runoob),
    url(r'^search/$', search.search),
    url(r'^search-form/$', search.search_form),
    path('testdb/',testdb.testdb),
    path('runoob/',views.runoob),
    path('getdata/',testdb.getdata),
    path('updatedb/',testdb.updatedb),
    path('deletedb/',testdb.deletedb),
    url(r'^admin/',admin.site.urls)
]
