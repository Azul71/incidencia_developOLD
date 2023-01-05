from django.db import models
from django.utils import timezone
from datetime import datetime,timedelta
from django.conf import settings

# Create your models here.


class Received(models.Model):
	name = models.CharField(max_length=100)
	created_on = models.DateTimeField(default=datetime.now)
	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Roles(models.Model):
	name = models.CharField(max_length=100)
	created_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.name


class Status(models.Model):
	title = models.CharField(max_length=50)
	created_on = models.DateTimeField(default=datetime.now)
	class Meta:
		ordering = ['title']

	def __str__(self):
		return self.title

class TypeFollowUp(models.Model):
	title = models.CharField(max_length=50)
	created_on = models.DateTimeField(default=datetime.now)
	class Meta:
		ordering = ['title']

	def __str__(self):
		return self.title

class Concello(models.Model):
	title = models.CharField(max_length=50)
	created_on = models.DateTimeField(default=datetime.now)
	class Meta:
		ordering = ['title']

	def __str__(self):
		return self.title
		



class Enquiry(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	nif = models.CharField(max_length=9)
	razonsocial = models.CharField(max_length=100)
	relation = models.CharField(max_length=100)
	address = models.TextField(blank=True,null=True)
	contact = models.CharField(max_length=9)
	email = models.CharField(max_length=50)

	status = models.ForeignKey(Status,on_delete=models.CASCADE)
	concello = models.ForeignKey(Concello,on_delete=models.CASCADE)
	received = models.ForeignKey(Received,on_delete=models.CASCADE)
	enquire = models.TextField(blank=True,null=True)
	typefollowup = models.ForeignKey(TypeFollowUp,on_delete=models.CASCADE)
	#rol = models.ForeignKey(Roles,on_delete=models.CASCADE,blank=True,null=True)
	register = models.DateTimeField(default=datetime.now)
	createdby = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='createdby')
	asigned = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='asigned')
	created_on = models.DateTimeField(default=datetime.now)
	#experience = models.CharField(max_length=2)
	#course_fee = models.CharField(max_length=7,blank=True,null=True,default=0)
	#batch = models.ForeignKey(Batch,on_delete=models.CASCADE,null=True,blank=True)
	#date_of_birth = models.DateField(blank=True,null=True)
	#qualification = models.CharField(max_length=100)
	#course_type = models.CharField(max_length=2)
	#expected_date = models.DateTimeField(blank=True,null=True)
	#lead_sourse = models.CharField(max_length=100)
	#lead_date = models.DateField(blank=True,null=True)
	#lms_id = models.CharField(max_length=2,default=0)
	#lms_username = models.CharField(max_length=50,blank=True,null=True)
	#tms_id = models.CharField(max_length=2,default=0)
	

	def __str__(self):
		return self.first_name


class Follow_ups(models.Model):
	enquiry = models.ForeignKey(Enquiry,on_delete=models.CASCADE)
	description = models.TextField(blank=True,null=True)
	date = models.DateTimeField(blank=True,null=True)
	typefollowup = models.ForeignKey(TypeFollowUp,on_delete=models.CASCADE)
	created_on = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return self.description

"""
class Batch(models.Model):
	title = models.CharField(max_length=100)
	trainer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,limit_choices_to={'role':'4'},blank=True,null=True)
	start_date = models.DateField(blank=True,null=True)
	end_date = models.DateField(blank=True,null=True)
	status = models.ForeignKey(Status,on_delete=models.CASCADE)
	received = models.ForeignKey(Received,on_delete=models.CASCADE)
	TYPES = [('0', 'Basic Training'),('1', 'On Job Training'),]
	course_type = models.CharField(max_length=2,choices=TYPES)
	#departament = models.ForeignKey(Departament,on_delete=models.CASCADE)
	DAYS = [('0', 'Weekdays'),('1', 'Weekends'),]
	days = models.CharField(max_length=2,choices=DAYS,default='0')
	class_start = models.TimeField(blank=True)
	class_end = models.TimeField(blank=True)
	created_on = models.DateTimeField(default=datetime.now)
	status = models.CharField(max_length=2,default=0)


	def __str__(self):
		return self.title


class account(models.Model):
	enquiry_id = models.ForeignKey(Enquiry,on_delete=models.CASCADE)
	detail = models.TextField(blank=True,null=True)
	date = models.DateTimeField(blank=True,null=True)
	amount = models.CharField(max_length=7,blank=True,null=True)
	created_on = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return self.detail

"""
