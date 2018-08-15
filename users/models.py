from datetime import date
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from allauth.socialaccount.models import SocialToken, SocialAccount

from .manager import UserManager

year_choices = [
        (None, 'Year'),
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
        (5,'Fifth'),
    ]

gender_choices = [
        (None,'Gender'),
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
]

class Events(models.Model):
    eventsList = models.TextField(null=True)


class College(models.Model):
    collegeName = models.CharField(max_length=250)
    regCount = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % self.collegeName


class KYProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=50, unique=True)
    full_name = models.CharField(max_length=130, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=gender_choices, null=True, blank=True,default=None)
    college = models.ForeignKey(College, null=True, blank=True)
    year = models.PositiveSmallIntegerField(choices=year_choices, null=True, blank=True)
    mobile_number = models.BigIntegerField(null=True, blank=True)

    profile_link = models.CharField(max_length=300, null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True, default='https://storage.forums.net/6479407/images/vagmAzMznjBJGQf_sumV.png')
    has_ca_profile = models.BooleanField(default=False)
    profile_completed = models.BooleanField(default=False)
    ky_id = models.CharField(max_length=20, null=True, blank=True)
    referralCode = models.CharField(max_length=20, null=True, blank=True) #should be caId of some CA.
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_paid = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=50,null=True,blank=True)
    paid_amt = models.IntegerField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.email

    def save(self, *args, **kwargs):
        if self.ky_id is None:
            try:
                temp = KYProfile.objects.all().order_by("-id")[0].id
                self.ky_id = 'KY%04d' % (temp + 101)
            except Exception as e:
                self.ky_id = 'KY%04d' % 101
        super(self.__class__, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" %(self.ky_id)

#instance is socialaccount, instance .user is kyprofile
def save_profile(sender, instance, **kwargs):
    instance.user.full_name = instance.extra_data['name']
    if instance.provider!='Google': #make sure the social app object's name is Google (case-sensitive)
        try:
           instance.user.gender = instance.extra_data['gender']
        except Exception as e:
            pass # sometimes google doesn't return gender :(
    instance.user.profile_link = instance.extra_data['link']
    instance.user.profile_picture = instance.get_avatar_url()
    instance.user.save()

post_save.connect(save_profile, sender=SocialAccount)


class CAProfile(models.Model):
    kyprofile = models.OneToOneField(KYProfile)

    whatsapp_number = models.BigIntegerField(null=True, blank=True)
    postal_address = models.TextField(null=True, blank=True)
    pincode = models.PositiveIntegerField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)

    regs = models.ManyToManyField(KYProfile, blank=True, related_name='regs')
    reg_num = models.PositiveIntegerField(default=0, null=True, blank=True) #no. of refered kyprofile.
    ca_id = models.CharField(max_length=20, null=True, blank=True)
    is_choosen = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.ca_id is None:
            try:
                temp = CAProfile.objects.all().order_by("-id")[0].id
                self.ca_id = 'KYCA%04d' % (temp + 101)
            except Exception as e:
                self.ca_id = 'KYCA%04d' % 101
        super(self.__class__, self).save(*args, **kwargs)


    def __str__(self):
        return "%s - %s" %(self.kyprofile.full_name, self.ca_id)
