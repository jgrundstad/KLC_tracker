from django.shortcuts import render
from django.http import HttpResponse

from tracker.models import Proceeding, Contact, Item, Code

# Create your views here.
def index(request):
  proceeding_list = Proceeding.objects.order_by('start_date')
  context = {'proceeding_list': proceeding_list}
  return render(request, 'tracker/index.html', context)


def item(request, item_id):
  return HttpResponse("Inspecting item %s." % item_id)


def contact(request, contact_id):
  return HttpResponse("Inspecting contact %s." % contact_id)


def items(request, proceeding_id):
  items = Item.objects.filter(proceeding=proceeding_id).order_by('-date')
  line_count_list = list()
  notes_list = list()
  contact_list = list()
  # get codes
  codes = Code.objects.all()
  for item in items:
    # replace code
    n = item.notes
    for c in codes:
      n = n.replace(c.code, c.value) 
    notes_list.append(n)
    # get line counts for sizing textareas
    count = str((item.notes).count('\n') + 3)
    line_count_list.append(count)
    # get list of contacts
    contact_string = ''
    for c in item.contacts.all():
      contact_string += "%s " % c.short_name
    contact_list.append(contact_string)
  item_list = zip(items, notes_list, line_count_list, contact_list)
  # get the proceeding name from the id to add to the heading
  p_name = Proceeding.objects.filter(id=proceeding_id)[0].name
  context = {'item_list': item_list, 'proceeding': p_name}
  return render(request, 'tracker/items.html', context)

