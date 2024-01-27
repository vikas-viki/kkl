from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('academics/', views.academics, name='academics'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('facility/', views.facilities, name='facilities'),
    path('ktc/', views.ktc, name="ktc"),
    path('kkp/', views.kkp, name="kkp"),
    path('iec/', views.iec, name="iec"),
    path('icscr/', views.icscr, name="icscr"),
    path('ibsc/', views.ibsc, name="ibsc"),
    path('contact/', views.contact, name="contact"),
    path('news/', views.news_kavi, name="news_kavi"),
    path('publications/', views.publications, name='publications'),
    path('collaborators/', views.collaborators, name='collaborators'),
    path('faculty/', views.faculty, name='faculty'),
    path('patent/', views.patents, name='patents'),
    path('projects/', views.projects, name='projects'),
    path('test/', views.test, name='test'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('bikul-das/', views.director, name='bikul-das'),
    path('director/', views.director, name='director'),
    path('sitemap.xml/',views.sitemap),
]
