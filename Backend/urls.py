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
from houses.views import CreateHouseView,GetHouseView,GetAllHouseView,SearchHousesView
import houses
from clients.views import RegistrationView, LoginView, LogoutView, ChangePasswordView, GetProfileView
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('accounts/register', RegistrationView.as_view(), name='register'),
    path('accounts/login', LoginView.as_view(), name='register'),
    path('accounts/logout', LogoutView.as_view(), name='register'),
    path('accounts/change-password', ChangePasswordView.as_view(), name='register'),
    path('accounts/token-refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/get-profile', GetProfileView.as_view(), name='get_profile'),
    path('houses/register', houses.views.CreateHouseView.as_view(), name='register_house'),
    path('houses/get-house', houses.views.GetHouseView.as_view(), name='get_house'),
    path('houses/get-houses', houses.views.GetAllHouseView.as_view(), name='get_all_houses'),
    path('houses/search-houses',houses.views.SearchHousesView.as_view(), name='get_all_houses'),
]
