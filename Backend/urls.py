"""Testing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import houses.views
from clients import views
from clients.views import RegistrationView, LoginView, LogoutView,ChangePasswordView, GetProfileView
from rest_framework_simplejwt import views as jwt_views
from houses.views import CreateHouseView
from django.conf.urls.static import static
from Backend import settings

urlpatterns = [
    path('accounts/register', RegistrationView.as_view(), name='register'),
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout', LogoutView.as_view(), name='logout'),
    path('accounts/change-password', ChangePasswordView.as_view(), name='change_password'),
    path('accounts/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/get-profile', GetProfileView.as_view(), name='get_profile'),
    path('houses/register', houses.views.CreateHouseView.as_view(), name='register_house')+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
