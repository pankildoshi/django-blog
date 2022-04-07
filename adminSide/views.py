from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from post_module.models import Post
from django.contrib.auth.models import User
 
def adminValidate(request):

	if(request.method == "POST"):
		adminName = request.POST['adminName']
		adminPword = request.POST['adminPword']

		if adminName == 'admin':
			if adminPword == 'admin':
				return HttpResponseRedirect('adminHome')
			else:
				messages.error(request,"Invalid Credentials")
				return redirect('adminValidate')
		else:
				messages.error(request,"Invalid Credentials")
				return redirect('adminValidate')
	else:
		return render(request,'adminLogin.html')

def adminH(request):
	b = Post.objects.all()
	return render(request,'adminHome.html',{'b':b})

def userDisplay(request):
	user = User.objects.all()
	return render(request,'displayUsers.html',{'user':user})

def deleteBlog(request):
    if(request.method == "POST"):
        postId = request.POST['id']
        post = get_object_or_404(Post, id=postId)
        post.delete()
        return HttpResponseRedirect('adminHome')
    else:
        return render(request,"adminHome.html")

def banUser(request):
    if(request.method == "POST"):
        userId = request.POST['id']
        p = get_object_or_404(User, id=userId)
        p.delete()
        return HttpResponseRedirect('displayUsers')
    else:
        return render(request,"displayUsers.html")
