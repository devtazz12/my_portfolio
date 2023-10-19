from django.contrib import admin
from .models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=['fname','email','subject']

admin.site.register(ContactMe, ContactAdmin)
