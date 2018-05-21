from django.db import models
from ..login_reg_app.models import User
from datetime import datetime
from datetime import date


class TravelManager(models.Manager):
	def basic_validator_create(self, postData, id):
		errors = {}
		if len(postData['destination']) < 1:
			errors['destination'] = 'Field must be filled in'
		if len(postData['description']) < 1:
			errors['description'] = 'Field must be filled in'
		if len(postData['start']) < 1:
			errors['start'] = 'Field must be filled in'
		else:
			start = postData['start']
			start_date = datetime.strptime(start, '%Y-%m-%d')
			if start_date < datetime.today():
				errors['start'] = 'Date must be current'
		if len(postData['end']) < 1:
			errors['end'] = 'Field must be filled in'
		else:
			end = postData['end']
			end_date = datetime.strptime(end, '%Y-%m-%d')
			if len(postData['start']) > 1:
				if end_date < start_date:
					errors['end'] = "End date cannot be before start date"
		print (errors)
		if len(errors) > 0:
			result = {
				'obj': errors,
				'status': False
			}
			return result
		else:
			user = User.objects.get(id=id)
			travel = Travel.objects.create(
				destination= postData['destination'],
				description= postData['description'],
				start= postData['start'],
				end= postData['end'],
				user_planned_it= User.objects.get(id=id)
				)
			user.travel_attending.add(travel)
			result = {
				'obj': travel.id,
				'status': True
			}
			return result


		
class Travel(models.Model):
	destination = models.CharField(max_length=255)
	description= models.CharField(max_length=255)
	start = models.DateField(auto_now=False)
	end = models.DateField(auto_now=False)
	user_planned_it = models.ForeignKey(User, related_name="planned_travel")
	user_attending = models.ManyToManyField(User, related_name="travel_attending")
	created_at = models.DateField(auto_now_add = True)
	updated_at = models.DateField(auto_now = True)
	objects = TravelManager()
