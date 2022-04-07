from django.urls import path
from django.urls.resolvers import URLPattern

from . import views
 
urlpatterns=[
	path('adminLogin', views.adminValidate, name='adminValidate'),
	path('adminHome', views.adminH, name='adminRedirect'),
	path('displayUsers',views.userDisplay, name='userDisplay'),
	path('deleteBlog',views.deleteBlog,name='deleteBlog'),
	path('banUser',views.banUser,name='banUser'),
]