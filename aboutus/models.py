from django.db import models

# Create your models here.

class WWB(models.Model):
	"""
	model for what we believe

	"""
	title = models.CharField(max_length=100)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Message(models.Model):
	"""
	model for what we believe

	"""
	title = models.CharField(max_length=100)
	content = models.TextField()
	notes = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class About(models.Model):
	name = models.CharField(max_length=100)
	content = models.TextField()
	slug = models.CharField(max_length=1, unique=True)

	def __str__(self):
		return self.name
