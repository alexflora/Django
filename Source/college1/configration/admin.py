from django.contrib import admin
from.models import Language,State,Country

admin.site.register(Language)
admin.site.register(State)
#admin.site.register(Country)

# Register your models here.
class stateinline(admin.TabularInline):
    model=State

@admin.register(Country)
class countryadmin(admin.ModelAdmin):
    inlines=[stateinline]
    

#if we use inline method we should write the 'get_queryset function' then only the value is populated in the inline table
def get_queryset(self,request):
    return Country.objects.filter(code="IN")    
    
   

