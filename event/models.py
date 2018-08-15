from django.db import models
from users.models import KYProfile

class ParentEvent(models.Model):
    parentEventId = models.AutoField(primary_key = True)
    categoryName = models.CharField(max_length = 50)

    def __str__(self):
        return "Category: %s" %self.categoryName


class Event(models.Model):
    eventId = models.AutoField(primary_key=True)
    eventName = models.CharField(max_length=50)
    eventDetails = models.TextField()
    maxMembers = models.PositiveSmallIntegerField(null=True,blank=True)
    minMembers = models.PositiveSmallIntegerField(null=True,blank=True)
    parentEvent = models.ForeignKey(ParentEvent)
    # parentEventId = models.PositiveSmallIntegerField(null=True,blank=True)

    def __str__(self):
        return 'Event:%s, EventId: %s, Category: %s' % ( self.eventName,self.eventId, self.parentEvent.categoryName, )

class Team(models.Model):
    teamName = models.CharField(max_length=250, null=True, blank=True)
    teamId = models.AutoField(primary_key = True)
    event = models.ForeignKey(Event)
    teamLeader = models.ForeignKey(KYProfile,related_name = 'teamLeader')
    members = models.ManyToManyField(KYProfile,related_name = 'members')

    def __str__(self):
        return 'Team Id: %s, Event: %s' %(self.teamId, self.event.eventName)

