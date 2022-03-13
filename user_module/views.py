from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
# Create your views here.
def login(request):

	if(request.method == "POST"):
		username = request.POST['name']
		email = request.POST['email']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']
		
		if pass1 == pass2:
			if(User.objects.filter(username=username).exists()):
				print("User name is not available")
			elif(User.objects.filter(email=email).exists()):
				print("Email is already taken")
			else:
				user=User.objects.create_user(username=username,password=pass1,email=email)
				user.save()
				print('User Created')
		else:
			print("Password Not Matching")
		return redirect('/')
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
			return redirect('userLogin')
	else:
		return render(request,"validateUser.html")

def logout_view(request):
    logout(request)
    return redirect('/')