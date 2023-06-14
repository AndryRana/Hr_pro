"""Candidates URL Configuration

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
from django.urls import path, include
from App import views
from Candidates import settings
from django.conf.urls.static import static

# Admin Panel (Replace)
admin.site.site_header = "HR ADMIN"
admin.site.index_title = "Table of candidates"

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # Frontend
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login/', include('django.contrib.auth.urls')),
    # Backend
    path('backend/', views.backend, name='backend'),
    path('<int:id>/', views.candidate, name='candidate'),
    path('delete/<int:id>/', views.delete, name='delete'),
    # Export to PDF
    path('<int:id>/index/', views.index, name='index'),
    path('pdf/<int:id>/', views.pdf, name='pdf'),
    # Send email
    path('email', views.email, name='email'),
    # Candidate (Chat group)
    path('chat_candidate/<int:id>/', views.chat_candidate, name='chat_candidate'),
    
    
    
]  + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
