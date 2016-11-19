from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django import forms
from .models import *
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
	list_display = ["__str__", "name", "content" ]
	class Meta:
		model = Contact

class AddressAdmin(SummernoteModelAdmin):
	list_display = ["__str__", "name"]
	class Meta:
		model = Address

admin.site.register(Contact, ContactAdmin)
admin.site.register(Address, AddressAdmin)

