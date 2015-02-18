from django.forms import ModelForm
from tracker.models import Item

class ItemForm(ModelForm):
  class Meta:
    model = Item
    fields = ['proceeding', 'name', 'notes', 'date']
