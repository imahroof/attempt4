from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import fetch_cve_vulnerabilities



urlpatterns = [
    path('api/set-csrf-token', views.set_csrf_token, name='set_csrf_token'),
    path('api/login', views.login_view, name='login'),
    path('api/logout', views.logout_view, name='logout'),
    path('api/user', views.user, name='user'),
    path('api/register', views.register, name='register'),
    path('api/fetch-ransomware-attacks/', views.fetch_ransomware_attacks),
    path("api/fetch-cves/", fetch_cve_vulnerabilities, name="fetch-cves"),
    path("dashboardget/", views.getDashboards,),
    path('dashboardpost/',views.postDashboard),
    path('dashboarddelete/', views.deleteDashboard, name='deleteDashboard'),
    path('dashboardaddwidget/', views.addWidget, name='addwidget'), 
    path('dashboarddeletewidget/', views.deleteWidget, name='deletewidget'), 
    path('dashboardcomplete/', views.dashboardcomplete, name='dashboardcomplete'),
]