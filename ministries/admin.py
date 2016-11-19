from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
# Register your models here.


class MenAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Men

class WomenAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Women

class YouthAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Youth

class ChildrenAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Children

class DonationAdmin(SummernoteModelAdmin):
	list_display = ["__str__", 'amount']
	class Meta:
		model = Donation

admin.site.register(Women, WomenAdmin)
admin.site.register(Donation, DonationAdmin)
admin.site.register(Men, MenAdmin)
admin.site.register(Youth, YouthAdmin)
admin.site.register(Children, ChildrenAdmin)