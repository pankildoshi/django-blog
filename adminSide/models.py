from django.db import models

# Create your models here.
class adminModel(models.Model):
	adminName=models.CharField(max_length=200)
	adminPassword=models.CharField(max_length=50)

	def __str__(self):
		return self.adminName
		