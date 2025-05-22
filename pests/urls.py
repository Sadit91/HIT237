from django.urls import path
from . import views
from .views import (
    FarmListView, FarmCreateView, FarmUpdateView, FarmDeleteView,
    SessionListView, SessionCreateView, SessionUpdateView, SessionDeleteView,
    ObservationListView, ObservationCreateView, ObservationUpdateView, ObservationDeleteView
)
from .views import grower_portal
from django.contrib.auth import views as auth_views
from .views import register
from .views import logout_view
from .views import effort_calculator



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.pro_list.as_view(), name='project_list'),
    path('project/<str:itype>/<int:pid>/', views.pro_det.as_view(), name='proj_detail'),
        # --- Farm URLs ---
    path('farms/', FarmListView.as_view(), name='farm_list'),
    path('farms/add/', FarmCreateView.as_view(), name='farm_add'),
    path('farms/<int:pk>/edit/', FarmUpdateView.as_view(), name='farm_edit'),
    path('farms/<int:pk>/delete/', FarmDeleteView.as_view(), name='farm_delete'),

    # --- Session URLs ---
    path('sessions/', SessionListView.as_view(), name='session_list'),
    path('sessions/add/', SessionCreateView.as_view(), name='session_add'),
    path('sessions/<int:pk>/edit/', SessionUpdateView.as_view(), name='session_edit'),
    path('sessions/<int:pk>/delete/', SessionDeleteView.as_view(), name='session_delete'),

    # --- Observation URLs ---
    path('observations/', ObservationListView.as_view(), name='observation_list'),
    path('observations/add/', ObservationCreateView.as_view(), name='observation_add'),
    path('observations/<int:pk>/edit/', ObservationUpdateView.as_view(), name='observation_edit'),
    path('observations/<int:pk>/delete/', ObservationDeleteView.as_view(), name='observation_delete'),
    
    # --- Grower Portal URL ---
    path("portal/", grower_portal, name="grower_portal"),

    # --- Authentication URLs ---
    path('accounts/register/', register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='pests/registration/login.html'), name='login'),
    path('accounts/logout/', logout_view, name='logout'),

    # --- Effort Calculator URL ---
    path('calculator/', effort_calculator, name='effort_calculator'),
]