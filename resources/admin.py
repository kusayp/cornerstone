from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
# Register your models here.


class SermonAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Sermon

class SermonCommentAdmin(SummernoteModelAdmin):
	list_display = ["__str__", "content"]
	class Meta:
		model = Comment

class SermonCategoryAdmin(SummernoteModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model = Tag

class DevotionAdmin(SummernoteModelAdmin):
	list_display = ["__str__", "date_posted"]
	class Meta:
		model = Devotion


admin.site.register(Sermon, SermonAdmin)
admin.site.register(Comment, SermonCommentAdmin)
admin.site.register(Tag, SermonCategoryAdmin)
admin.site.register(Devotion, DevotionAdmin)
