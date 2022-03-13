from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns=[
	path('login',views.login,name='login'),
	path('validateUser', views.validateUser, name='userLogin'),
	path('logout',views.logout_view,name='logout'),
]