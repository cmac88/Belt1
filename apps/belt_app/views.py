from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..login_reg_app.models import User
from .models import *
from datetime import datetime
today = date.today()


def index(request):
	if 'user' not in request.session:
		return redirect('/login_reg')
	print(request.session['user'])
	user = User.objects.get(id=request.session['user'])
	travel = Travel.objects.all()
	context = {
		'user_info': User.objects.get(id=request.session['user']),
		'trips_user': user.travel_attending.all(),
		'trips_not_user': travel.exclude(user_attending=user.id),
		'all_users': User.objects.all()
	}



	return render(request, 'belt_app/index.html', context)

def logout(request):
	request.session.clear()
	return redirect('/login_reg')

def add(request):
	if 'user' not in request.session:
		return redirect('/login_reg')
	return render(request, 'belt_app/travel_add.html')

def create(request):
	if 'user' not in request.session:
		return redirect('/login_reg')
	print(request.POST)
	travel = Travel.objects.basic_validator_create(request.POST, request.session['user'])
	if travel['status'] == False:
		for key, value in travel['obj'].items():
			messages.error(request, value, extra_tags = key)
		return redirect('/belt/add')
	else:
		return redirect('/belt')
	return redirect('/belt')

def destination(request, id):
	if 'user' not in request.session:
		return redirect('/login_reg')
	travel = Travel.objects.get(id = id)
	user = User.objects.get(id = request.session['user'])
	context={
		'destination': travel,
		'attending': travel.user_attending.exclude(id = user.id)
	}
	print(context)
	return render(request, 'belt_app/destination.html', context)

def join(request, id):
	if 'user' not in request.session:
		return redirect('/login_reg')
	user = User.objects.get(id = request.session['user'])
	trip = Travel.objects.get(id=id)
	trip.user_attending.add(user) 
	return redirect('/belt')


