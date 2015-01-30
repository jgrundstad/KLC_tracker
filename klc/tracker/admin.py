from django.contrib import admin
from tracker.models import Proceeding, Client, Item, Code

class ProceedingAdmin(admin.ModelAdmin):
  list_display = ('name', 'client', 'start_date')

class ItemAdmin(admin.ModelAdmin):
  list_display = ('proceeding', 'date', 'name', 'snippet')

  def snippet(self, obj):
    return "%s..." % obj.notes[0:24]
  snippet.short_description = 'notes snippet'

class ClientAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'short_name', 'role', 'phone1', 'email')
  
  def full_name(self, obj):
    return ("%s, %s" % (obj.last_name, obj.first_name))

  full_name.short_description = 'full name'

class CodeAdmin(admin.ModelAdmin):
  list_display = ('code', 'snippet')

  def snippet(self, obj):
    return "%s..." % obj.value[0:30]

  snippet.short_description = 'code snippet'

# Register your models here.
admin.site.register(Proceeding, ProceedingAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Code, CodeAdmin)
