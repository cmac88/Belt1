from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
	def basic_validator_create(self, postData):
		errors = {}
		if len(postData['name']) < 1:
			errors['name'] = 'Name must be filled in'
		elif len(postData['name']) < 3:
			errors['name'] = 'Name must be at least three characters'
		if len(postData['username']) < 1:
			errors['user'] = 'Username must be filled in'
		if len(postData['username']) < 3:
			errors['user'] = 'Username must be at least 3 characters'
		if len(postData['pw']) < 1:
			errors['password'] = 'Password must be filled in'
		elif len(postData['pw']) < 8:
			errors['password'] = 'Password must be at least eight characters long'
		if len(postData['confirm_pw']) < 1:
			errors['confirm_pw'] = 'Confirm password must be filled in'
		elif postData['confirm_pw'] != postData['pw']:
			errors['confirm_pw'] = 'Confirm password must match password'
		print(errors)
		if len(errors) > 0:
			result = {'obj': errors, 'status': False}
			print(result)
			return result
		else:
			user = User.objects.create(
			name = postData['name'], 
			username= postData['username'],
			password= bcrypt.hashpw(postData['pw'].encode(), bcrypt.gensalt()))
			result = {'obj': user.id, 'status': True}
			return result

	def basic_validator_login(self, postData):
		errors = {}
		if len(postData['username']) < 1:
			errors['logu'] = 'Username must be filled in'
		if len(postData['pw']) < 1:
			errors['login_pw'] = 'Password must be filled in'
		if len(errors) > 0:
			result = {'obj': errors, 'status': False}
			return result
		if not User.objects.filter(username=postData['username']):
			errors['le'] = 'Could not be logged in'
		if len(errors) > 0:
			result = {'obj': errors, 'status': False}
			print(result)
			return result
		else:
			user = User.objects.get(username=postData['username'])
			print(user)
			result = {'obj': user.id, 'status': True }
			return result


class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()


