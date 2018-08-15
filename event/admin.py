# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from event.models import *

from django.contrib import admin
admin.site.register(Event)
admin.site.register(ParentEvent)


# Register your models here.
class TeamAdmin(admin.ModelAdmin):

    def college(obj):
        return obj.teamLeader.college.collegeName

    list_display = ('event', 'teamName', 'teamId', 'teamLeader', college)
    search_fields = ('event__eventName', 'teamName', 'teamId', 'teamLeader__ky_id', 
    					'teamLeader__college__collegeName')

admin.site.register(Team, TeamAdmin)