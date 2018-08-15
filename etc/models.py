from django.db import models
from users.models import CAProfile
from collections import defaultdict
from django.utils import timezone
from datetime import datetime, tzinfo, timedelta

# Create your models here.

class Notifications(models.Model):
	text = models.CharField(max_length=2000)
	users = models.ManyToManyField(CAProfile, blank=True)
	read_by = models.ManyToManyField(CAProfile, blank=True, related_name='mark_read')
	recieved_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.text

class Post(models.Model):
	message = models.TextField(null=True, blank=True)
	created_time = models.DateTimeField(null=True, blank=True)
	pid = models.CharField(max_length=100, unique=True)#post id
	link = models.URLField(null=True, blank=True)
	full_picture = models.URLField(null=True, blank=True)
	picture = models.URLField(null=True, blank=True)
	show = models.BooleanField(default=True)

	def __str__(self):
		return str(self.link)

class PublicRelation(models.Model):
	ca = models.ForeignKey(CAProfile)
	related_to = models.CharField(max_length=200)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	contact = models.BigIntegerField()
	designation = models.CharField(max_length=200)
	college = models.CharField(max_length=200)

	def __str__(self):
		return str(self.ca)


class Point(models.Model):
	ca = models.ForeignKey(CAProfile)
	pr_points = models.IntegerField(default=0)
	fb_points = models.IntegerField(default=0)
	extra_points = models.IntegerField(default=0)
	reg_points = models.IntegerField(default=0)
	payment_points = models.IntegerField(default=0)
	total_points = models.IntegerField(null=True, blank=True)

	def save(self, *args, **kwargs):
		self.total_points = self.pr_points + self.fb_points + self.reg_points + self.extra_points + self.payment_points
		super(self.__class__, self).save(*args, **kwargs)

	def __str__(self):
		return '%s - %s' %(self.ca.ca_id, self.ca.kyprofile.full_name)



class MobileNotification(models.Model):
	body = models.TextField()
	image_url = models.URLField(null=True, blank=True)
	link = models.URLField(null=True, blank=True)
	timestamp = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return '%s - %s' % (self.pk, self.body)
	