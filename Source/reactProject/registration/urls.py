from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register('personal', personalview)
router.register('country', countryview)
router.register('language', languageview)

urlpatterns = [
    path('', include(router.urls))
]
