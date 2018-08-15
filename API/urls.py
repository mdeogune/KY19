from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from API.views import *

router = routers.DefaultRouter()
router.include_format_suffixes = False
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^current_user/$', current_user),
    url(r'^posts/$', posts),
    url(r'^notifications/$', notifications),
    url(r'^public-relations/$', publicRelationsView.as_view()),
    url(r'^all-notifications/$', all_notifications),
    url(r'^leaderboard/$', leaderboard),
    url(r'^ca-profile/$', CAProfileUpdate),
    url(r'^ky-profile/$', KYProfileUpdate),
    url(r'^updatecauser/$', updateCAUser),
    url(r'^all-event/$', allEvent),
    url(r'^teamregister/$', registerTeam),
    url(r'^get-reg/$', getReg),
    url(r'^indregister/$', registerIndi),
    url(r'^deleteteam/$', deleteteam),
    url(r'^referedreg/$', getReferedReg),

    url(r'^sub-event/(?P<eventName>[\w|\W]+)$',subEvent),

    ##mobile app
    url(r'^mobile/login/$', mobileLogin),
    url(r'^mobile/register/$', mobileRegister),
    url(r'^mobile/notifications/$', mobileNotifications),

    url(r'^mobile/login/social/$', mobileSocialLogin),


]

urlpatterns = format_suffix_patterns(urlpatterns)