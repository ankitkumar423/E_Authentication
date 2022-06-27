from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login as lgin,logout as lgout,authenticate

# Create your views here.

def signup(request):
	if request.method == "POST":
		fn = request.POST['fname']
		ln = request.POST['lname']
		ec = request.POST['empcode']
		em = request.POST['email']
		pwd = request.POST['pass']
		try:
			user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
			EmployeeDetail.objects.create(user=user,empcode=ec)
			error="no"
		except:
			error="yes"

	return render(request,'signup.html',locals())

def login(request):
	if request.method == "POST":
		e = request.POST['mail']
		p = request.POST['emppass']
		user=authenticate(username=e,password=p)
		if user:
			lgin(request,user)
			error="no"
		else:
			error="yes"

	return render(request,'emplogin.html',locals())

def home(request):
	if not request.user.is_authenticated:
		return redirect('login')
	return render(request,'emp_base.html');

def changepass(request):
	if not request.user.is_authenticated:
		return redirect('login')
	return render(request,'changepassadmin.html')

def logout(request):
	lgout(request)
	return redirect('signup')

	
def changepass(request):
	if not request.user.is_authenticated:
		return redirect('login')
	user=request.user
	if request.method == "POST":
		c = request.POST['curpass']
		n = request.POST['npass']

		if user.check_password(c):
			user.set_password(n)
			user.save()
			error="no"
		else:
			error="not"

	return	render(request,'changepass.html',locals())


def forgotpass(request):
	if request.method == "POST":
		c = request.POST['curmail']
		n = request.POST['npass']
		try:
			user = User.objects.get(username=c)
			user.set_password(n)
			user.save()
			error="no"
		except:
			error="not"
	return	render(request,'forgotpass.html',locals())

