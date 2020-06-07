from django.contrib import admin
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'title')
    list_display_links = ('id','username')
    search_fields = ('id', 'username', 'title','email', 'phone', 'message')

admin.site.register(Contact, ContactAdmin)
