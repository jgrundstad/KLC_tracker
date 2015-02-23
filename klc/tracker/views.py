from django.shortcuts import render
from django.http import HttpResponse
from forms import ItemForm
from tracker.models import Proceeding, Contact, Item, Code

# Create your views here.
def index(request):
  proceeding_list = Proceeding.objects.order_by('start_date')
  context = {'proceeding_list': proceeding_list}
  return render(request, 'tracker/index.html', context)


def new_item(request, proceeding_id):
  # add-new-item form
  form = ItemForm(request.POST)
  context = {'form': form, 'proceeding_id': proceeding_id}
  return render(request, 'tracker/new_item.html', context)


def create_new_item(request, proceeding_id):
  if request.method == 'POST':
    form = ItemForm(request.POST)
    form.save()
    return HttpResponse("Thanks")



def item(request, item_id):
  return HttpResponse("Inspecting item %s." % item_id)


def contact(request, contact_id):
  return HttpResponse("Inspecting contact %s." % contact_id)


def items(request, proceeding_id):
  items = Item.objects.filter(proceeding=proceeding_id).order_by('date')
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
    contacts = list()
    emails = list()
    for c in item.contacts.all():
      #contacts.append(c.short_name + '\n' + c.email)
      contacts.append(c.short_name)
      emails.append("%s, %s\n%s\n%s" % (c.last_name, c.first_name,
        c.email, c.phone1))
    contact_list.append(zip(contacts, emails))
  item_list = zip(items, notes_list, line_count_list, contact_list)
  # get the proceeding name from the id to add to the heading
  p_name = Proceeding.objects.filter(id=proceeding_id)[0].name
  context = {'item_list': item_list, 'proceeding': p_name, 'proceeding_id': proceeding_id}
  return render(request, 'tracker/items.html', context)

