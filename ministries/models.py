from django.db import models

# Create your models here.

class Men(models.Model):
	"""
	model for Men

	"""
	name = models.CharField(max_length=100)
	content = models.TextField()
	time = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	contacts = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Women(models.Model):
	"""
	model for Women

	"""
	name = models.CharField(max_length=100)
	content = models.TextField()
	time = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	contacts = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Youth(models.Model):
	"""
	model for Youth

	"""
	name = models.CharField(max_length=100)
	content = models.TextField()
	time = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	contacts = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Children(models.Model):
	"""
	model for Children

	"""
	name = models.CharField(max_length=100)
	content = models.TextField()
	time = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	contacts = models.CharField(max_length=500)

	def __str__(self):
		return self.name

class Donation(models.Model):
	MINISTRY_TO = (
		('', 'Please select which ministry you want to donate to'),
		('Men', 'Men Fellowship'),
		('Women', 'Women Fellowship'),
		('Children', 'Children Fellowship'),
		('Youth', 'Youth Fellowship'),
		)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	city = models.CharField(max_length=100)
	address =  models.CharField(max_length=500)
	ministry = models.CharField(max_length=10, choices=MINISTRY_TO)
	amount = models.CharField(max_length=10)

	def __str__(self):
		return self.firstname

# class Leader(models.Model):
# 	name: