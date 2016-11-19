from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
# Register your models here.

class EventAdmin(SummernoteModelAdmin):
	list_display = ["__str__", "begin_date", "location"]
	class Meta:
		model = Event

class EventCategoryAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Category

class EventRegisterAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Register

class WordAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Word

admin.site.register(Event, EventAdmin)
admin.site.register(Category, EventCategoryAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Register, EventRegisterAdmin)
