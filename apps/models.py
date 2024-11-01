from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Model, ForeignKey, CASCADE, Manager, CharField, AutoField, BinaryField, UniqueConstraint, \
    IntegerField, CheckConstraint, Q, DateTimeField, DateField, DurationField
from django_jsonform.models.fields import JSONField


# Create your models here.


class Products(Model):
    name = models.CharField(max_length=100, db_comment="product_name")
    price = models.FloatField()
    category = ForeignKey('apps.Category', on_delete=CASCADE, related_name='products')


class Category(Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    count = models.IntegerField(default=0)

    class Meta:
        db_table = 'category'  # table name to database
        db_table_comment = "for categories"  # for table comment

        get_latest_by = ['name']  # take the latest
        ordering = ['name']  # for ordering categories
        permissions = ()  # for special permission
        unique_together = ('name', 'price')  # this provide will unique together


class OrderedCategory(Category):
    class Meta:
        proxy = True
        ordering = ['-name']


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
    joined_at = DateField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)


class Event(Model):
    SCHEMA = {
    'type': 'dict',
    'keys': {
        'age': {
            'type': 'number',
            'title': 'Age in years',
            'default': 50, # default value for age
        },
        'favorite' :{
            'type': 'string',
        }
    },
}
    name = CharField(max_length=100)
    duration = DurationField(timedelta(hours=2, minutes=30))
    description = JSONField(schema=SCHEMA, null=True, blank=True)


#  =======================  Shell =========================
# Event.objects.create(
#     name='Sirk',
#     duration=timedelta(hours=2, minutes=30),
#     description={   "age": 18, "favorite": "tiger"  }
# )

# Event.objects.filter(description__favorite="tiger")
#  =======================  Shell =========================



