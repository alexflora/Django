from.views import *
from django.urls import path

urlpatterns = [
    path('domain/',domain),
    path('hr/',HR),
    path('employee/',employee),
    path('worker/',worker),
]
