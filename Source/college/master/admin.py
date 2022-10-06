from django.contrib import admin
from .models import Department, Staff, Country, State
# Register your models here.


class StateInline(admin.TabularInline):
    model = State


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    radio_fields = {"gender": admin.HORIZONTAL}
    readonly_fields = ('staff_code',)
    ordering = ('-name',)
    search_fields = ('name',)

    # filter_horizontal = ('name',) # only to many2many fields
    # exclude = ('name',) # To hide the field in form

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(gender="Male")


admin.site.register(Department)
# admin.site.register(Staff)
admin.site.register(State)

# admin.site.register(Country)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):

    inlines = [StateInline]