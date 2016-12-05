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
	expectation = models.CharField(max_length=500)
	involved = models.CharField(max_length=500)

	def __str__(self):
		return self.title

class Question(models.Model):
	question = models.CharField(max_length=100)
	anwser = models.CharField(max_length=500)

	class Meta:
		verbose_name_plural = 'Common Questions People Ask'

	def __str__(self):
		return self.question

class About(models.Model):
	name = models.CharField(max_length=100)
	content = models.TextField()
	slug = models.CharField(max_length=1, unique=True)

	def __str__(self):
		return self.name
