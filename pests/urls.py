from django.urls import re_path
from . import views  # Import the class-based views

urlpatterns = [
    # Home page
    re_path(r'^$', views.home, name='home'),
    
    # About page
    re_path(r'^about/$', views.about, name='about'),
    
    # Project List View
    re_path(r'^projects/$', views.pro_list.as_view(), name='project_list'),
    
    # Project Detail View
    re_path(r'^project/(?P<pid>\d+(-[a-z0-9-]+)?)/$', views.pro_det.as_view(), name='proj_detail'),
]
