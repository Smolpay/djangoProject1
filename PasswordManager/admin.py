

# Register your models here.
from django.contrib import admin
from .models import TableKey



# Define the admin class
class TableKeyAdmin(admin.ModelAdmin):
        list_display = ('forWhat', 'password', 'published_date')
        list_filter = ('forWhat', 'created_date', 'published_date', 'name')

# Register the admin class with the associated model
admin.site.register(TableKey, TableKeyAdmin)