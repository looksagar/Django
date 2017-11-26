from django.contrib import admin
from .models import post
from .models import student
# Register your models here.
admin.site.register(post)
admin.site.register(student)


#class PostModelAdmin(admin.ModelAdmin):
	#list_display = ["title","updated","timestamp"]
	#list_display_links = ["updated"]
	#list_editable = ["title"]
	#list_filter = ["updated","timestamp"]
	#search_fields = ["title","content"]
	#class Meta:
		#model = post


#admin.site.register(post,PostModelAdmin)