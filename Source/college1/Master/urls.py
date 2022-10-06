from operator import imod
from django.contrib import admin
from django.urls import path,include
from.views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Student',Studentview)

urlpatterns = [path('api/',include(router.urls))]
"""path('mypage/',test),
               path('mytable/',table),
               path('dep/create',dep)"""