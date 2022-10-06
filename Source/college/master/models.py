from django.db import models


class Department(models.Model):

    name = models.CharField("Name", max_length=255, null=True, blank=True)
    code = models.CharField("Code", max_length=255, null=True, blank=True)
    hod = models.OneToOneField("master.Staff", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=True)
    staff_code = models.CharField("Staff Code", max_length=255, null=True, blank=True)
    gender = models.CharField("Gender", choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=False)
    code = models.CharField("Code", max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=False)
    code = models.CharField("Code", max_length=255, null=True, blank=True)
    country = models.ForeignKey("master.Country", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

