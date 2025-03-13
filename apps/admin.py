from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(ContactToUser)
class ContactToUserAdmin(admin.ModelAdmin):
    list_display = ['name','email']

@admin.register(UserProjects)
class UserProjectsAdmin(admin.ModelAdmin):
    list_display = ['name','description']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['OwnerImage','OwerName']

@admin.register(UserResume)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['file','date_update']