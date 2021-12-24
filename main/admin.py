from django.contrib import admin
from .models import *


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


class PointAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'address', 'pid')
    list_display_links = ('id', 'city', 'address', 'pid')
    search_fields = ('id', 'city')


class MedicineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'qua', 'price', 'code', 'manufacture', 'pid')
    list_display_links = ('id', 'name',)
    search_fields = ('id', 'name', 'code', 'pid')


admin.site.register(City, CityAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Medicine, MedicineAdmin)

admin.site.site_title = '24Аптека'
