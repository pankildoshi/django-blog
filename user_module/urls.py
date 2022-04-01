from django.urls import path
from django.urls.resolvers import URLPattern
from .views import UserUpdateView
from . import views

urlpatterns=[
	path('login', views.login, name='login'),
	path('validateUser', views.validateUser, name='userLogin'),
	path('logout',views.logout_view,name='logout'),
	path('update_profile', UserUpdateView.as_view(), name='update_profile'),
]