from django.db import models

# Create your models here.

class Verse(models.Model):
	"""
	model for welcome

	"""
	verse = models.CharField(max_length=100, blank=True)
	verse_text = models.TextField(blank=True)


	def __str__(self):
		return self.verse

class Pastor(models.Model):
	"""
	model for pastors

	"""
	date_posted = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
	ministry = models.CharField(max_length=100)
	languages = models.CharField(max_length=100)
	fav_verse = models.CharField(max_length=300)
	background = models.TextField()
	phone = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	img_url = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class Subscribe(models.Model):
	email = models.EmailField(max_length=254)

	def __str__(self):
		return self.email

class Welcome(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()

	def __str__(self):
		return self.title
