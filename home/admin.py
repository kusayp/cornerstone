from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
# Register your models here.


class VerseAdmin(SummernoteModelAdmin):
	list_display = ["__str__", "verse_text"]
	class Meta:
		model = Verse


class PastorAdmin(SummernoteModelAdmin):
	list_display = ["__str__", "name"]
	class Meta:
		model = Pastor

class SubscribeAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Subscribe

class WelcomeAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Welcome

admin.site.register(Verse, VerseAdmin)
admin.site.register(Pastor, PastorAdmin)
admin.site.register(Welcome, WelcomeAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
