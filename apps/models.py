from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Model, ForeignKey, CASCADE, Manager, CharField, AutoField, BinaryField


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



class User(AbstractUser):
    pass

    def clean(self):
        super().clean()
        if self.username.lower() == "botir":
            raise ValidationError('Botir  taqiqlanadi')