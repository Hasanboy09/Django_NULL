from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import Job, Student, Event, Teacher, Boy, Month, Category, Product, ProductImage, Films, Genres


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    search_fields = ['description__age', 'description__favorite']  # json search with value
    list_display = 'name', 'description__age'

    @admin.display(description='Age')
    def description__age(self, obj: Event):
        return obj.description['age']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Boy)
class BoyAdmin(admin.ModelAdmin):
    pass


@admin.register(Month)
class MonthAdmin(admin.ModelAdmin):
    pass


# ==========================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass



@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass



@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    pass


@admin.register(Genres)
class FilmsAdmin(ModelAdmin):
    pass


