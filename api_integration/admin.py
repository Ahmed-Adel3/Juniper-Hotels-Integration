from django.contrib import admin
from .models import Zone, City, HotelCategory, Hotel, HotelDoLog

# Register your models here.
admin.site.register(Zone)
admin.site.register(City)
admin.site.register(HotelCategory)

class HotelAdmin(admin.ModelAdmin):
    search_fields = ('jp_code', 'name')

admin.site.register(Hotel, HotelAdmin)

# Logs
@admin.register(HotelDoLog)
class HotelDoLogAdmin(admin.ModelAdmin):
    list_display = ('method', 'error', 'created_date')
    list_filter = ('error',)
    actions = ['export_to_csv']
