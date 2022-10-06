from django.contrib import admin
from.models import *

admin.site.register(Domains)
#admin.site.register(Hr_domain)
admin.site.register(Employee)
admin.site.register(workers)

@admin.register(Hr_domain)
class domainhr (admin.ModelAdmin):
    list_display=['name','Domains']
    


# Register your models here.
