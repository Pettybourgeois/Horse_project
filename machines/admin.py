from django.contrib import admin

# Register your models here.
from .models import Machine
class MachineAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'status', 'function',)
    list_display_links = ('id','title')
    search_fields = ('id', 'title', 'status', 'function',)

admin.site.register(Machine, MachineAdmin)   


