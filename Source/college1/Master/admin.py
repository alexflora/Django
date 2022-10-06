from django.contrib import admin
from.models import Department,Staff,Student

admin.site.register(Department)
admin.site.register(Staff)
admin.site.register(Student)
# Register your models here.


"""@admin.register(Student)
class StudentAdmin (admin.ModelAdmin):
    #Recored level
    #Add column for viewing purpose
    list_display=['Name','Gender','department','state','country']
    #add filter to a perticular column or (more then one column list_filter=['country','state']
    list_filter=['country']
    #ordering-ascending or desending (ordering=['-Name'])
    ordering=['Name']
    
    #field level
    #two column layout
    #------------------fields=(('Name','department'),('state','country'),'Age','Gender','email')
    
    #remove the field from the layout
    #exclude=('Age',)
    
    #read only field 
    readonly_fields=['email']
    
    #radio_field
    radio_fields={'Gender':admin.HORIZONTAL}
    
    #fieldsets -- for make heading for the details and also make fields 
    fieldsets=(("Basic",{"fields":(('Name','Age','Gender'))}),("personal",{"fields":(('state','country'))}))
    
    #search fields
    search_fields=['Name']
    
    #fillter the charfield
    def get_queryset(self,request):
        #rec=super().get_queryset(request)
        #return rec.filter(Gender="Male") 
        return Student.objects.filter(Name="Alexander")
    
    #fillter the relation field 
    def get_queryset(self,request):
        rec=super().get_queryset(request)
        return rec.filter(state__state='alex')"""
    
   
