from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout
from .views import *

urlpatterns = [
	url(r'^ky-team/$', teamPage, name= 'events_index'),
	url(r'^sponsors/$', sponsorsPage, name= 'events_index'),
	url(r'^schedule/$', schedulePage, name= 'schedulePage'),

	url(r'^contact/$', contactPage, name= 'events_index'),

]