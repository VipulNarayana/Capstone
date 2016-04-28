from django.db import models

# Create your models here.
class Vehicle(models.Model):
	vehicle=models.CharField(max_length=10)
	flag=models.IntegerField(null=True)
	time=models.TimeField(null=True)
	count=models.IntegerField(null=True)
	def __str__(self):
		return self.vehicle + ' ' + str(self.flag) + ' ' +str(self.time)+ ' ' + str(self.count)
