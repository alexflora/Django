import re
from django.db import models
# Create your models here.


class Country(models.Model):
    name = models.CharField("Country", max_length=255, null=False, blank=False)
    code = models.CharField("code", max_length=30, null=True, blank=False)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=False)
    code = models.CharField("code", max_length=30, null=True, blank=False)


class personal(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=False)
    age = models.IntegerField("Age", null=True, blank=False)
    gender = models.CharField("Gender", choices=[(
        'male', 'Male'), ('female', 'Female')], max_length=30, null=True, blank=False)
    dob = models.DateField("DOB", null=True, blank=False)
    phone = models.IntegerField("Phone", null=True, blank=False)
    email = models.EmailField("Email", null=True, blank=True)
    pincode = models.IntegerField("Pincode", null=True, blank=True)
    country = models.ForeignKey(
        Country, verbose_name="Country", on_delete=models.SET_NULL, null=True, blank=False)

    def __str__(self):
        return self.name
