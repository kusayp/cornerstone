from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

from .models import *
# Register your models here.

class HymnAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	search_fields = ('name','refrain')
	class Meta:
		model = Hymn

class CategoryAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Category

class StanzaAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Stanza

admin.site.register(Hymn, HymnAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Stanza, StanzaAdmin)