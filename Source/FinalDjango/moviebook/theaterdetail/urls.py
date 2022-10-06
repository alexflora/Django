from rest_framework import routers
from django.urls import path, include
from .views import *
from moviedetail.views import *
from bookingdetail.views import *
from user.views import *

router = routers.DefaultRouter()
router.register('branch', Branchview)
router.register('theater', Theaterview)
router.register('hall', Hallview)
router.register('role', Roleview)
router.register('employee', Employeeview)
router.register('movie',  moviewview)
router.register('show', Showview)
router.register('language', Languageview)
router.register('booking', Bookingview)
router.register('customer', Customerview)
router.register('payment', Paymentview)
router.register('status', Statusview)
router.register('user', Userview)

urlpatterns = [
    path('api/', include(router.urls))
]
