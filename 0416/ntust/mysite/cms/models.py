from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length = 20)
	birthday = models.DateField('your birthday')
	gender =  models.BooleanField('girl?', default = True)
	def __str__(self):
		return self.name