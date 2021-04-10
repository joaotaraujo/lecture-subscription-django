"""lecture_subscription URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.views.generic import RedirectView
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/lecture_system/')),
    path('lecture_system/', views.initial_screen),
    path('lecture_system/submit', views.submit_ticket),
    path('lecture_system/search_screen/', views.search_screen),
    path('lecture_system/search_screen/submit', views.search_ticket),
    path('lecture_system/ticket_info_screen/<int:ticket_id>/', views.ticket_info_screen),
    path('lecture_system/login/', views.adm_screen),
    path('lecture_system/login/submit', views.submit_login),
    path('lecture_system/logout/', views.logout_user)
]
