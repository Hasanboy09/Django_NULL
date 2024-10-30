from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.models import Job, User


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(UserAdmin):
    pass