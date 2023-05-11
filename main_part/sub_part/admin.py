from django.contrib import admin

# Register your models here.
from . models import *
admin.site.register(register_table)

admin.site.register(admission_table)

admin.site.register(contact_table)