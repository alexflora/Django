import email
from email.headerregistry import Address
from email.policy import default

from numpy import require
from theaterdetail.models import *
from moviedetail.models import *
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import CustomUser
from django.contrib.auth.models import Group
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
import socket


class Customer(models.Model):
    name = models.CharField("Name", max_length=100, null=True, blank=False)
    dob = models.DateField("DOB", null=True, blank=False)
    age = models.CharField("Age", max_length=20, null=True, blank=False)
    gender = models.CharField("Gender", max_length=20, choices=[(
        'male', 'Male'), ('female', 'Female'), ('others', 'Others')])
    phone = models.CharField("Phone", max_length=10, null=True, blank=False)
    email = models.EmailField("Email", null=True, blank=False)
    address = models.TextField("Address", null=True, blank=True)
    ctype = models.CharField(
        "CustomerType", max_length=100, null=True, blank=True, default='NewCustomer')

    def __str__(self):
        return str(self.name)

    # def save(self):
    #     res = super(Customer, self).save()
    #     return res

    def save(self):
        # socket.getaddrinfo('localhost', 8000)
        res = super().save()
        context = {"username": self.name, "password": self.phone}
       # send_mail("New Worker", "Welcome to our newly opened company!",
        #         "peter", ['suriyaalbert@gmail.com'])
        msg = EmailMultiAlternatives(subject='Login Credential', from_email='alexander94255@gmail.com', to=[
                                     'suriyaalbert@gmail.com'], cc=['mervinalfred007@gmail.com'])
        html_template = get_template(
            "Email.html").render(context)
        msg.attach_alternative(html_template, "text/html")
        msg.send()
        return res


@receiver(post_save, sender=Customer)
def event_attender_create(sender, instance, *args, **kwargs):
    if instance and kwargs['created']:
        user = CustomUser.objects.create(email=instance.email, username=instance.name.lower(),
                                         customer=instance, role="NewCustomer", is_staff=True)
        user.set_password(instance.phone)
        if instance.ctype == "NewCustomer":
            if Group.objects.filter(name='NewUser').exists():
                user.groups.add(Group.objects.get(name='NewUser'))
        print('==============', user)
        user.save()
    return True


class Status(models.Model):
    name = models.CharField("Status", max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name


class Booking(models.Model):
    customername = models.CharField(
        "CustomerName", max_length=100, null=True, blank=False)
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, null=True, blank=False)
    # status = models.ForeignKey(
    #     Status, on_delete=models.RESTRICT, null=True, blank=False)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, null=True, blank=False)
    hall = models.ForeignKey(
        Hall, on_delete=models.CASCADE, null=True, blank=False)
    halltype = models.CharField("HallType", max_length=100, choices=[(
        'a/c', 'A/C'), ('normal', 'Normal')], null=True, blank=False)
    noofseats = models.IntegerField("NoOfSeats", null=True, blank=False)
    totalamount = models.FloatField("TotalAmount", null=True, blank=False)

    def __str__(self):
        return str(self.customername)


class Payment(models.Model):
    name = models.ForeignKey(
        Booking, verbose_name="CoustomerName", on_delete=models.CASCADE, null=True, blank=False)
    type = models.CharField("PaymentType", max_length=50, choices=[
                            ('online', 'Online'), ('offline', 'Offline')])

    def __str__(self):
        return str(self.name.customername)

    def save(self):
        res = super().save()
        context = {"name": self.name. customername,
                   "movie": self.name.movie.name,
                   "hall": self.name.hall.name,
                   "noofseats": self.name.noofseats,
                   "amount": self.name.totalamount,
                   "theater": self.name.branch.theatername.name}
        msg = EmailMultiAlternatives(subject='Paid Details', from_email='alexander94255@gmail.com', to=[
                                     'denish2000jul@gmail.com'], cc=['mervinalfred007@gmail.com'])
        html_template = get_template(
            "pay.html").render(context)
        msg.attach_alternative(html_template, "text/html")
        msg.send()
        return res

# Create your models here.
