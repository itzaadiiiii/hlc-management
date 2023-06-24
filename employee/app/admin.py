from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(employee)   
# @admin.register(department)

admin.site.register(employee)
admin.site.register(department)