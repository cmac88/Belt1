from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User

def index(request):

	users = User.objects.all()
	# print(users.values())
	return render(request,'login_reg_app/index.html')

def create(request):
	# print(request.POST)
	user = User.objects.basic_validator_create(request.POST)
	print(user)
	if user['status'] == False:
		for key, value in user['obj'].items():
			messages.error(request, value, extra_tags = key)
		return redirect('/login_reg')
	else:
		request.session['user'] = user['obj']
		return redirect('/belt')

def login(request):
	user = User.objects.basic_validator_login(request.POST)
	print('user', user)
	if user['status'] == False:
		for key, value in user['obj'].items():
			messages.error(request, value, extra_tags = key)
		return redirect('/login_reg')
	else:
		request.session['user'] = user['obj']
		return redirect('/belt')

def profile(request):
	context = {
		'user': User.objects.get(id=request.session['user'])
	}
	return render(request,'login_reg_app/profile.html', context)



