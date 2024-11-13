from datetime import timedelta

import requests
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Model, Manager, CharField, BinaryField, UniqueConstraint, \
    IntegerField, CheckConstraint, Q, DateTimeField, DateField, DurationField, SlugField, URLField, \
    PositiveIntegerField, ForeignKey, CASCADE
from django.utils import timezone
from django.utils.text import slugify
from django_jsonform.models.fields import JSONField


# Create your models here.


# class Products(Model):
#     name = models.CharField(max_length=100, db_comment="product_name")
#     price = models.FloatField()
#     category = ForeignKey('apps.Category', on_delete=CASCADE, related_name='products')
#
#
# class Category(Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(decimal_places=2, max_digits=10)
#     count = models.IntegerField(default=0)
#
#     class Meta:
#         db_table = 'category'  # table name to database
#         db_table_comment = "for categories"  # for table comment
#
#         get_latest_by = ['name']  # take the latest
#         ordering = ['name']  # for ordering categories
#         permissions = ()  # for special permission
#         unique_together = ('name', 'price')  # this provide will unique together


# class OrderedCategory(Category):
#     class Meta:
#         proxy = True
#         ordering = ['-name']

class SalleManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(namme__icontains='sale')


class Job(Model):
    name = CharField(max_length=100)
    # price = AutoField(primary_key=True ) # automatic generate price with order(tartib)
    count = models.BigAutoField(db_comment="job_name", primary_key=True)
    image = BinaryField()


class Bag(Model):
    name = CharField(max_length=100)

    class Meta:
        select_on_save = True


class User(AbstractUser):
    def save(self, *args, **kwargs):
        if 'botir' in self.username.lower():
            raise ValidationError('Username atmen!')

        super().save(*args, **kwargs)


class Employee(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    price = IntegerField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=('first_name', 'last_name'), name='unique_employee'),
            CheckConstraint(check=Q(price__gt=0), name='price must be greater than 0'),

        ]
        required_db_vendor = 'postgresql'


class Student(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    joined_at = DateField(auto_now=True)  # only date
    created_at = DateTimeField(auto_now_add=True)  # time and date


class Event(Model):
    SCHEMA = {
        'type': 'dict',
        'keys': {
            'age': {
                'type': 'number',
                'title': 'Age',
                'default': 50,  # default value for age
            },
            'favorite': {
                'type': 'string',
            }
        },
    }
    name = CharField(max_length=100)
    duration = DurationField(timedelta(hours=2, minutes=30))
    description = JSONField(schema=SCHEMA, null=True, blank=True)

    def __str__(self):
        return self.name


#  =======================  Shell =========================
# Event.objects.create(
#     name='Sirk',
#     duration=timedelta(hours=2, minutes=30),
#     description={   "age": 18, "favorite": "tiger"  }
# )

# Event.objects.filter(description__favorite="tiger")
#  =======================  Shell =========================


class Teacher(Model):
    name = CharField(max_length=100)
    slug = SlugField(unique=True, blank=True, editable=False)
    link = URLField(max_length=200, unique=True)

    def save(self, *args, init_id=None, **kwargs):
        self.slug = slugify(self.name)
        if not init_id:
            self.save(*args, init_id=True, **kwargs)
            self.slug += f"-{self.id}"
        super().save(*args, **kwargs)


class Boy(Model):
    name = CharField(max_length=100)
    link = URLField(max_length=200, unique=True)

    def clean(self):
        try:
            response = requests.head(self.link, allow_redirects=True)
            if response.status_code != 200:
                raise ValidationError(f"The link {self.link} is not valid.")
        except requests.RequestException as e:
            raise ValidationError(f"The link {self.link} could not be reached: {e}")


#  ======================================  Task 1 ==================================================
#
# class Category(Model):
#     uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = CharField(max_length=100)
#
#
# class Product(Model):
#     uuid = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = CharField(max_length=100)
#     price = IntegerField()
#     category = ForeignKey('apps.Category', on_delete=CASCADE, related_name='products')
#

# ================================= Task 2 ============================================================


# class Time(Model):
#     country = CharField(max_length=100)
#     created_at = TimeField()
#     changed_at = DateTimeField()
#
#     # , default = timezone.now


# ===================================   1-  variant ========================================================

# class Category(Model):
#     id = BigAutoField(unique=True, primary_key=True)
#     uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     name = CharField(max_length=100)
#     slug = SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
#
#
# class Product(Model):
#     name = CharField(max_length=100)
#     category = ForeignKey('apps.Category', on_delete=CASCADE)


# ===================================   2-  variant ========================================================

# class Category(Model):
#     id = BigAutoField(unique=True, primary_key=True)
#     uuid = UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     name = CharField(max_length=100)
#     slug = SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
#
#
# class Product(Model):
#     name = CharField(max_length=100)
#     category = ForeignKey('apps.Category', on_delete=CASCADE ,to_field='uuid')


import calendar


def time_valid(value):
    time = timezone.now().minute
    if time % 2 != 0:
        raise ValidationError(f"Vaqt {timezone.now()} juft emas.")
    return value


class Month(Model):
    month = IntegerField(choices=enumerate(list(calendar.month_name)[1:], start=1), validators=[time_valid])

    def __str__(self):
        return list(calendar.month_name)[self.month]


# =======================================================================================



class Category(Model):
    name = CharField(max_length=100)

    class Meta:
        db_table = 'category'


class Product(Model):
    name = CharField(max_length=100)
    price = PositiveIntegerField(default=1000)
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
    count = PositiveIntegerField(default=10)


    class Meta:
        db_table = 'product'

