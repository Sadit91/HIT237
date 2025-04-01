# In pests/urls.py, using regex for more flexible URL matching:
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^projects/$', views.proj_list, name='proj_list'),
    re_path(r'^project/(?P<pid>\d+(-[a-z0-9-]+)?)/$', views.proj_det, name='proj_detail'),
    re_path(r'^about/$', views.about, name='about'),
]
