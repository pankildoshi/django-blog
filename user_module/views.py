from re import template
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .forms import UserUpdateForm
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .models import Contact
# Create your views here.
def login(request):

	if(request.method == "POST"):
		username = request.POST['name']
		email = request.POST['email']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']
		fname = request.POST['fname']
		lname = request.POST['lname']

		if pass1 == pass2:
			if(User.objects.filter(username=username).exists()):
				print("User name is not available")
			elif(User.objects.filter(email=email).exists()):
				print("Email is already taken")
			else:
				user=User.objects.create_user(username=username,password=pass1,email=email)
				user.first_name = fname
				user.last_name = lname
				user.save()
				print('User Created')
		else:
			print("Password Not Matching")
		return redirect('login')
	else:
		return render(request,'login.html')

def validateUser(request):
	if(request.method == "POST"):
		loginUser = request.POST['loginUser']
		loginPassword = request.POST['loginPassword']
		
		user = authenticate(username=loginUser,password=loginPassword)
		if user is not None:
			auth_login(request,user)
			return redirect("/")
		else:
			messages.error(request,"Invalid Credentials")
			return redirect('login')
	else:
		return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def about(request):
	return render(request, 'about.html')

class UserUpdateView(UpdateView):
	model = User
	form_class = UserUpdateForm
	template_name = 'update_profile.html'
	success_url = reverse_lazy('profile')

	def get_object(self):
		return self.request.user

class PasswordUpdateView(PasswordChangeView):
	model = User
	form_class = PasswordChangeForm
	template_name = 'update_password.html'
	success_url = reverse_lazy('profile')

class ContactView(CreateView):
	model = Contact
	fields = '__all__'
	template_name = 'contact.html'
	success_url = reverse_lazy('index')