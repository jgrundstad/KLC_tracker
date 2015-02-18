from django.db import models
from django.forms import ModelForm

# Create your models here.

class Client(models.Model):
  first_name = models.CharField(max_length=128)
  last_name = models.CharField(max_length=128)
  short_name = models.CharField(max_length=32)
  role = models.CharField(max_length=128, blank=True)
  company = models.CharField(max_length=128, blank=True)
  address1 = models.CharField(max_length=128, blank=True)
  address2 = models.CharField(max_length=128, blank=True)
  city = models.CharField(max_length=64, blank=True)
  state = models.CharField(max_length=16, blank=True)
  zipcode = models.CharField(max_length=12, blank=True)
  phone1 = models.CharField(max_length=24, blank=True)
  phone2 = models.CharField(max_length=24, blank=True)
  fax = models.CharField(max_length=24, blank=True)
  email = models.EmailField(max_length=128, blank=True)

  def __str__(self):
    return self.company


class Proceeding(models.Model):
  name = models.CharField(max_length=128)
  client = models.ForeignKey(Client)
  start_date = models.DateTimeField()
  CHOICES = (
      ('Y', 'Y'),
      ('N', 'N'),
  )
  archive = models.CharField(max_length=1, choices=CHOICES, default='N')
  
  def __str__(self):
    return self.name


class Item(models.Model):
  proceeding = models.ForeignKey(Proceeding)
  name = models.CharField(max_length=256)
  notes = models.TextField(blank=False, default='')
  date = models.DateTimeField()

  def __str__(self):
    return self.name


class Code(models.Model):
  code = models.CharField(max_length=32)
  value = models.TextField(max_length=512)
  


