from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import datetime,timedelta
#from enquiry.models import City,Departament

class Departament(models.Model):
	name = models.CharField(max_length=100)
	created_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.name
	
ROLE = [('2', 'Administrator'),('3', 'User')]

class CustomUser(AbstractUser):
	rol_interno = models.CharField(max_length=2,choices=ROLE,default='2')
	departament = models.ForeignKey(Departament,on_delete=models.CASCADE,blank=True,null=True)
	phone = models.CharField(max_length=10, blank=True)
	# REQUIRED_FIELDS = ['mobile', 'email']





