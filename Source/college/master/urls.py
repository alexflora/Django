from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router=routers.SimpleRouter()
router.register("staff",staffview)
router.register("country",countryview,basename='Alex')

app_name = 'master'
urlpatterns = [
    #path('department/', department_view),
    #path('department/create', department_create),
    #path('department/edit/<int:id>', department_update),
    #path('department/delete/<int:id>', department_delete),
    #path('staff/', staff_view),
    #path('staff/create',staff_create),
    #path('staff/edit/<int:id>',staff_update),
    #path('staff/delete/<int:id>',staff_delete),
    path('api/',include(router.urls)),
]
