from django.db import models


# Create your models here.

class Event(models.Model):
    """
    model for welcome"""

    organizer = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    details = models.TextField()
    location = models.CharField(max_length=300)
    begin_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    mobile = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    is_free = models.BooleanField(default=True)
    price = models.CharField(max_length=3, blank=True, null=True, default='')

    def __str__(self):
        return self.name


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    event = models.ForeignKey(Event, related_name='registration', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Word(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content
