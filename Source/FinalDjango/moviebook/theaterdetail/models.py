from pyexpat import model
from tabnanny import verbose
from django.db import models
from moviedetail.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import CustomUser
from django.contrib.auth.models import Group


class Theater(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=False)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=False)
    phone = models.CharField("Phone", max_length=10, null=True, blank=False)
    email = models.EmailField("Email", null=True, blank=False)
    address = models.TextField("Address", null=True, blank=False)
    theatername = models.ForeignKey(
        Theater, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return str(self.name)


class Hall(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=False)
    halltype = models.CharField(max_length=20, choices=[(
        'a/c', 'A/c'), ('normal', 'Normal')], null=True, blank=False)
    totalseat = models.IntegerField("TotalSeats", null=True, blank=False)
    branchid = models.ForeignKey(
        Branch, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return self.name


class Role (models.Model):
    name = models.CharField(
        "EmployeeType", max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField("Name", max_length=255, null=True, blank=False)
    dob = models.DateField("DOB", null=True, blank=False)
    age = models.IntegerField("Age", null=True, blank=False)
    gender = models.CharField(
        "Gender", max_length=20, choices=[('male', 'Male'), ('female', 'Female')])
    phone = models.CharField("Phone", max_length=10, null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    role = models.ForeignKey(
        Role, verbose_name='Role', on_delete=models.CASCADE, null=True, blank=False)
    aadharno = models.CharField(
        "AadharNo", max_length=12, null=True, blank=False)
    experience = models.IntegerField("Experience", null=True, blank=False)
    accountno = models.CharField(
        "AccountNo", max_length=20, null=True, blank=False)
    salary = models.FloatField("Salary", null=True, blank=False)
    address = models.TextField("Address", null=True, blank=False)
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Employee)
def event_attender_create(sender, instance, *args, **kwargs):
    if instance and kwargs['created']:
        user = CustomUser.objects.create(first_name=instance.name, email=instance.email, username=instance.name.lower(),
                                         employee=instance, role="Employee" if instance.role == "Employee" else "Manager", is_staff=True)
        user.set_password(instance.phone)
        if instance.role.name == "Employee":
            if Group.objects.filter(name='Employee').exists():
                user.groups.add(Group.objects.get(name='Employee'))
        else:
            if Group.objects.filter(name='Manager').exists():
                user.groups.add(Group.objects.get(name='Manager'))
        user.save()
    return True
