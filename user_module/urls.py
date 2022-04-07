from django.urls import path
from .views import UserUpdateView, ContactView, PasswordUpdateView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
	path('login', views.login, name='login'),
	path('validateUser', views.validateUser, name='userLogin'),
	path('logout',views.logout,name='logout'),
	path('update_profile', UserUpdateView.as_view(), name='update_profile'),
	path('update_password', PasswordUpdateView.as_view(), name='update_password'),
	path('contact', ContactView.as_view(), name='contact'),
	path('about', views.about, name='about'),
]