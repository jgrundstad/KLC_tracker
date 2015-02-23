from django.conf.urls import patterns, url

from tracker import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^(?P<item_id>\d+)/item/$', views.item, name='item'),
    url(r'^(?P<contact_id>\d+)/contact/$', views.contact, name='contact'),
    url(r'^(?P<proceeding_id>\d+)/items/$', views.items, name='items'),
    url(r'^(?P<proceeding_id>\d+)/new_item/$', views.new_item, name='new_item'),
    url(r'^(?P<proceeding_id>\d+)/create_new_item/$', views.create_new_item, name='create_new_item'),
  )
