from django import forms
from django.forms import ModelForm
from tracker.models import Item

class ItemForm(ModelForm):
  class Meta:
    model = Item
    fields = ['proceeding', 'contacts', 'name', 'notes']
