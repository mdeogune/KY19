from django.conf.urls import url, include
from django.shortcuts import redirect
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.defaults import page_not_found
from django.contrib.auth.views import logout
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView

from .settings import STATICFILES_DIRS

def lafda(request, shit):
    return redirect('/')

urlpatterns = [
    url(r'^(?P<shit>[\w{}.-]{5})/', lafda),
    url(r'^api/', include('API.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^ky-the-admin/', admin.site.urls),
    # url(r'^account/social/signup/',TemplateView.as_view(template_name='ca-redirect.html')),
    url(r'^account/email',page_not_found, {'exception': Exception('Not Found')}),
    url(r'^account/signup/$',lambda x: redirect('/form')),
    url(r'^account/login/$', lambda x: redirect('/account/facebook/login/')),
    url(r'^account/password/',page_not_found, {'exception': Exception('Not Found')}),
    # url(r'^account/confirm-email',page_not_found, {'exception': Exception('Not Found')}),
    url(r'^account/', include('allauth.urls')),
    url(r'^', include('users.urls')),
    url(r'^', include('etc.urls')),
    url(r'^',include('event.urls')),
    url(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
        RedirectView.as_view(url='/static/%(path)s', permanent=False)),
]

