from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Status)
admin.site.register(Booking)
admin.site.register(Payment)

# Register your models here.
