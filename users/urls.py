from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout
from .views import *
from . import views

urlpatterns = [
    url(r'^$', IndexView),
    url(r'^ca/$', CAIndexView),
#     url(r'^form/$', FormView),
    url(r'^user-form/$', UserFormView),
    url(r'^ca-form/$', CaFormView),
    url(r'^email_reg/$', EmailRegistration),
    url(r'^dashboard', DashboardView, name="ca-dashboard"),
    url(r'^privacy_policy/$', PrivacyPolicyView,),
    url(r'^reset_/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.reset_, name='reset_'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    
    url(r'^logout/$', LogoutView),
    url(r'^eventRegister/$', eventRegister),
    url(r'^forgotPass/$', forgotPassword),

]
