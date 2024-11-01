from django.contrib import admin

from apps.models import Job, Student, Event


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ['description__age', 'description__favorite'] # json search with value

