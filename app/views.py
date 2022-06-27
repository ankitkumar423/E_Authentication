from django.shortcuts import render

# Create your views here.

def signup(request):
	return render(request,'signup.html');

def login(request):
	return render(request,'emplogin.html');

def home(request):
	return render(request,'emp_base.html');

def changepass(request):
	return render(request,'changepassadmin.html')

def logout(request):
	return render(request,'signup.html');
	
