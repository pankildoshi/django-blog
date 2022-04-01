from dataclasses import fields
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.views import generic
from django.urls import reverse_lazy
from .forms import UserUpdateForm
from django.views.generic import CreateView
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
    logout(request)
    return redirect('/')

def about(request):
	return render(request, 'about.html')

class UserUpdateView(generic.UpdateView):
	model = User
	form_class = UserUpdateForm
	template_name = 'update_profile.html'
	success_url = reverse_lazy('profile')

	def get_object(self):
		return self.request.user

class ContactView(CreateView):
	model = Contact
	fields = '__all__'
	template_name = 'contact.html'
	success_url = reverse_lazy('index')