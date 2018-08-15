from django.conf.urls import url, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.contrib import admin
from event.views import *

app_name='event'

urlpatterns = [
	
	url(r'^events/$', eventPage, name= 'events_index'),
	url(r'^events/(?P<eventCatName>[\w|\W]+)$', eventCatPage, name= 'events_category_reg'),
	url(r'^events/teamRegister/(?P<eventName>[\w|\W]+)$', eventRegistration, name= 'events_reg'),
	url(r'^events/individualRegister/$', individualReg, name= 'ind_reg'),
	url(r'^regCheck/$', regCheckAjax, name= 'events_reg'),


]
