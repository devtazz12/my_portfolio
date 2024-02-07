from django.contrib import admin
from .models import *

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'subject']
admin.site.register(Contact, ContactAdmin)

admin.site.register(SocialMediaUrl)
admin.site.register(MyWork)
admin.site.register(MyCV)
