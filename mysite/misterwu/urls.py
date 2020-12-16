from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('user/',views.user,name="user"),
    path('teacher/',views.teacher,name='teacher')
]