from django.shortcuts import render
from django.http import HttpResponse

from tracker.models import Proceeding, Client, Item, Code

# Create your views here.
def index(request):
  proceeding_list = Proceeding.objects.order_by('start_date')
  context = {'proceeding_list': proceeding_list}
  return render(request, 'tracker/index.html', context)


def item(request, item_id):
  return HttpResponse("Inspecting item %s." % item_id)


def contact(request, contact_id):
  return HttpResponse("Inspecting contact %s." % contact_id)


def proceedings(request, proceeding_id):
  item_list = Item.objects.filter(proceeding=proceeding_id).order_by('-date')
  print "looking for proceeding_id: %s" % proceeding_id
  p_name = Proceeding.objects.filter(id=proceeding_id)[0].name
  context = {'item_list': item_list, 'proceeding': p_name}
  return render(request, 'tracker/proceedings.html', context)

