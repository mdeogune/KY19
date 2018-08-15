from rest_framework import serializers
from users.models import KYProfile, CAProfile
from etc.models import *
from event.models import *

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    ca_id = serializers.CharField(source='caprofile.ca_id', allow_blank=True)
    college = serializers.CharField(source='college.collegeName', allow_blank=True)

    class Meta:
        model = KYProfile
        fields = ('ca_id', 'ky_id', 'email', 'full_name', 'gender', 'profile_link',
        			'college', 'year', 'mobile_number', 'profile_picture','is_paid', 
                    'payment_id', 'paid_amt')


class PointSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='ca.kyprofile.full_name', allow_blank=True)
    college = serializers.CharField(source='ca.kyprofile.college.collegeName', allow_blank=True)

    class Meta:
        model = Point
        fields = ('name', 'college', 'total_points')

class CASerializer(serializers.ModelSerializer):

    class Meta:
        model = CAProfile
        fields = ('ca_id', 'whatsapp_number', 'pincode', 'postal_address')
        
class KYSerializer(serializers.ModelSerializer):
    college = serializers.CharField(source='college.collegeName', allow_blank=True)

    class Meta:
        model = KYProfile
        fields = ( 'ky_id', 'email', 'full_name', 'gender',
                    'college', 'year', 'mobile_number','is_paid')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('message', 'pid', 'link', 'full_picture', 'picture')


class MobileNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileNotification
        fields = ('body', 'image_url', 'link', 'timestamp')


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ('text', 'recieved_date')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentEvent 
        fields = ('parentEventId', 'categoryName')
        
class SubEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = ('eventId', 'eventName', 'eventDetails', 'maxMembers', 'minMembers', 'parentEvent')

class TeamSerializer(serializers.ModelSerializer):
    # ky_id = serializers.CharField(source='members_set.kyprofile.ky_id', allow_blank=True)

    members = KYSerializer(read_only=True, many=True)
    teamLeader = KYSerializer(read_only=True)
    class Meta:
        model = Team 
        fields = ('teamName', 'teamId', 'event', 'teamLeader', 'members')
class ReferedSerializer(serializers.ModelSerializer):
    # ky_id = serializers.CharField(source='members_set.kyprofile.ky_id', allow_blank=True)

    regs = KYSerializer(read_only=True, many=True)
 
    class Meta:
        model = CAProfile 
        fields = ('regs','ca_id')
class PublicRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicRelation
        fields = ('pk', 'related_to', 'name', 'email', 'contact', 'designation',
                    'college')

