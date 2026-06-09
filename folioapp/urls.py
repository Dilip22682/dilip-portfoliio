from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    path('success/', views.success, name='success'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/login/', views.dashboard_login, name='dashboard_login'),
    path('dashboard/logout/', views.dashboard_logout, name='dashboard_logout'),

    # Profile
    path('dashboard/profile/', views.profile_form, name='profile_form'),

    # Skills
    path('dashboard/skill/add/', views.skill_form, name='skill_form'),
    path('dashboard/skill/delete/<int:pk>/', views.skill_delete, name='skill_delete'),

    # Projects
    path('dashboard/project/add/', views.project_form, name='project_form'),
    path('dashboard/project/delete/<int:pk>/', views.project_delete, name='project_delete'),

    # Experience
    path('dashboard/experience/add/', views.experience_form, name='experience_form'),
    path('dashboard/experience/delete/<int:pk>/', views.experience_delete, name='experience_delete'),

    # Education
    path('dashboard/education/add/', views.education_form, name='education_form'),
    path('dashboard/education/delete/<int:pk>/', views.education_delete, name='education_delete'),
]