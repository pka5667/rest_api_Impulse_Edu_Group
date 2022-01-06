from django.contrib import admin
from .models import Assignment

# Register your models here.
# @admin.register(Assignments)
# class Assignment_Admin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'description', 'email']

admin.site.register(Assignment)
