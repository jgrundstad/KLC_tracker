from django.contrib import admin
from tracker.models import Proceeding, Client, Item
# Register your models here.
admin.site.register(Proceeding)
admin.site.register(Client)
admin.site.register(Item)
