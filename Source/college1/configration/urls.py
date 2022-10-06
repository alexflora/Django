from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register('State', StateView)
router.register('Country', CountryView)
urlpatterns = [path('api/', include(router.urls))]
