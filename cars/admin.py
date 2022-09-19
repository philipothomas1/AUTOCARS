from django.contrib import admin
from .models import Make,Trannsmission,Drive,FuelType,Color,Cars,BodyType,AutoParts,ContactInfomation,HomeBanner1,HomeBanner2,SideBanner1,SideBanner2,SideBanner3

# Register your models here.


class MakeAdmin(admin.ModelAdmin):
    list_display = ['id','make_name']
    list_filter = ['make_name']

    search_fields = ['make_name']

class CarsAdmin(admin.ModelAdmin):
    list_display = ['car_name', 'make','price','mileage','transmission','fueltype','engine']
    list_filter = ['car_name',]

    search_fields = ['car_name']

class AutoPartsAdmin(admin.ModelAdmin):
    list_display = ['spare_parts_name', 'category','make','price','condition']
    list_filter = ['spare_parts_name',]

    search_fields = ['spare_parts_name']

class ContactInfomationAdmin(admin.ModelAdmin):
    list_display = ['phone_number1', 'phone_number2','location','email','bank_account_number']
    list_filter = ['phone_number1',]

    search_fields = ['phone_number1']


admin.site.register(Make,MakeAdmin)
admin.site.register(Trannsmission)
admin.site.register(Drive)
admin.site.register(FuelType)
admin.site.register(Color)
admin.site.register(Cars,CarsAdmin)
admin.site.register(BodyType)
admin.site.register(AutoParts,AutoPartsAdmin)
admin.site.register(ContactInfomation,ContactInfomationAdmin)

admin.site.register(HomeBanner1)
admin.site.register(HomeBanner2)
admin.site.register(SideBanner1)
admin.site.register(SideBanner2)
admin.site.register(SideBanner3)



admin.site.site_header='Kapandila Motors, Adminstration Panel'
admin.site.site_title='Kapandila Motors'
admin.site.index_title='Kapandila Motors, Adminstration Panel'


