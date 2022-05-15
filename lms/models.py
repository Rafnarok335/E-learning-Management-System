from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class LMS_User(models.Model):

	User_Name = models.CharField(max_length=100)
	password = models.TextField()
	User_type = models.TextField()
	#auto_now=True or auto_now_add=True
	