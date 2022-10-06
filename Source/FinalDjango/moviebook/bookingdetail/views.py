from rest_framework import viewsets
from .serializer import *
from .models import *


class Bookingview (viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = Bookingserializer


class Statusview(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = Statusserializer


class Paymentview(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = Paymentserializer


class Customerview(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customerserializer
