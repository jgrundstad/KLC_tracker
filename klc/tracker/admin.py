from django.contrib import admin
from tracker.models import Proceeding, Client, Item

class ProceedingAdmin(admin.ModelAdmin):
  list_display = ('name', 'client', 'start_date')

class ItemAdmin(admin.ModelAdmin):
  list_display = ('proceeding', 'date', 'name', 'minutes_spent')

class ClientAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'company', 'phone1', 'email')
  
  def full_name(self, obj):
    return ("%s, %s" % (obj.last_name, obj.first_name))

  full_name.short_description = 'full name'


# Register your models here.
admin.site.register(Proceeding, ProceedingAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Item, ItemAdmin)
