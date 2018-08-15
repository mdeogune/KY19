from django.shortcuts import render,HttpResponseRedirect,redirect,Http404, HttpResponse, render_to_response
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import authentication_classes, permission_classes

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
import json

from API.serializers import *
from users.models import *
from users.apis import *
from etc.models import *
from event.models import *
from itertools import chain

class UserViewSet(viewsets.ModelViewSet):
	permission_classes = (permissions.IsAdminUser,)
	queryset = KYProfile.objects.all()
	serializer_class = UserSerializer

class publicRelationsView(APIView):
	def get(self, request, format=None):
		ca = request.user.caprofile
		prs = PublicRelation.objects.filter(ca=ca)
		serializer = PublicRelationSerializer(prs, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = PublicRelationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(ca=request.user.caprofile)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def current_user(request, format=None):
	serializer = UserSerializer(request.user)
	return Response(serializer.data)


@api_view(['GET'])
def leaderboard(request, format=None):
	top_points = Point.objects.all().order_by('-total_points')[:10]
	response = PointSerializer(top_points, many=True)
	ca_points = PointSerializer(Point.objects.get(ca=request.user.caprofile))

	data = {
		'top_points': response.data,
		'ca_points': ca_points.data
	}
	return Response(data)


@api_view(['GET'])
def posts(request):
	posts = Post.objects.filter(show=True).order_by('-created_time')
	serializer = PostSerializer(posts, many=True)
	return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def mobileNotifications(request):
	notices = MobileNotification.objects.all()
	serializer = MobileNotificationSerializer(notices, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def getReg(request):
	kyprofile = request.user
	team=Team.objects.filter(teamLeader=kyprofile) | Team.objects.filter(members=kyprofile)

	serializer = TeamSerializer(team, many=True)
	#print((serializer.data))

	return Response(serializer.data)


@api_view(['GET'])
def getReferedReg(request):
	KY = request.user
	ca=CAProfile.objects.get(kyprofile=KY)
	
	regs = KYProfile.objects.filter(referralCode=ca.ca_id)
	serializer=KYSerializer(regs, many=True)

	return Response(serializer.data)
	

@api_view(['POST'])
def deleteteam(request):
	#print("agaya")
	response_data={}
	post = request.data
	
	name=post.get('event',0)
	#print(name)
	
	Team.objects.filter(teamId=name).delete()
	

	response_data['status'] = 'deleted'
	return HttpResponse(
		json.dumps(response_data),
		content_type = "application/json"
		)


@api_view(['GET'])
def notifications(request):
	ca = request.user.caprofile
	usersnotices = Notifications.objects.filter(users=ca)
	unread = usersnotices.exclude(read_by=ca).order_by('-id')[:5]
	read = usersnotices.filter(read_by=ca).order_by('-id')
	unread_data = NotificationSerializer(unread, many=True).data
	read_data = NotificationSerializer(read[:(5 -len(unread))], many=True).data
	data = {
		'read': read_data,
		'unread': unread_data
	}
	return Response(data)


@api_view(['GET'])
def CAProfileUpdate(request):
	user = UserSerializer(request.user)
	ca = CASerializer(request.user.caprofile)
	data = {
		'user': user.data,
		'ca': ca.data
	}
	return Response(data)


@api_view(['GET'])
def KYProfileUpdate(request):
	user = UserSerializer(request.user)
	
	data = {
		'user': user.data,
		
	}
	return Response(data)


@api_view(['GET'])
def all_notifications(request):
	ca = request.user.caprofile
	notices = Notifications.objects.filter(users=ca).order_by('-id')
	notices = NotificationSerializer(notices, many=True)
	return Response(notices.data)


@api_view(['GET'])
def allEvent(request):
	
	parentevents=ParentEvent.objects.all()
	data = {}
	for index, pe in enumerate(parentevents):
		events = Event.objects.filter(parentEvent=pe)
		events = SubEventSerializer(events, many=True)
		data[pe.categoryName] = events.data

	return Response(data)


@api_view(['GET'])
def subEvent(request,eventName):
	event2=ParentEvent.objects.get(categoryName=eventName)
	#print(event2)
	#print(event2.event_set.all)
	event = Event.objects.filter(parentEvent=event2)
	#print(event)
	sub_event = SubEventSerializer(event,many =True)
	
	data = {
		'sub_event': sub_event.data,
		
	}
	#print (eventName)
	#print (sub_event)
	return Response(data)
	

@api_view(['POST'])
def updateCAUser(request):
	#print("aagaya")
	#print(request)

	try:
		post = request.data
		kyprofile = request.user
		kyprofile.mobile_number = post.get('mobile_number', 0)
		kyprofile.save()
		try:
			ca = kyprofile.caprofile
			ca.whatsapp_number = post.get('whatsapp_number', 0)
			ca.postal_address = post.get('postal_address', '')
			ca.pincode = post.get('pincode', 0)
			ca.save()
		except Exception as e:
			pass
		return Response(status=status.HTTP_200_OK)
	except Exception as e:
		return Response(e)


def regCheck(request, kyprofile, event):
	response_data = {}
	#print ('checking ', kyprofile)
	alreadyReg = False
	try:
		t=Team.objects.get(event=event, teamLeader=kyprofile)
		#print(t)
		#print("got")
		alreadyReg = True
	except :
		try:
			Team.objects.get(event=event, members=kyprofile)
			alreadyReg = True
		except :
			pass

	return alreadyReg


@api_view(['POST'])
def registerTeam(request):
	response_data = {}

	# try:
	post = request.data
	
	name=post.get('name',0)
	event_=post.get('event',0)
	team_leader=post.get('team_leader',0)
	members=post.get('member')
	team_leader=KYProfile.objects.get(ky_id = team_leader)
	
	event = Event.objects.get(eventName=event_)
	#print("team:")
	#print(team_leader)
	#print(regCheck(request, team_leader, event))
	if regCheck(request, team_leader, event):
		#print ('alreadyRe111g')
				
		response_data['status']= '%s already registered for event : %s.' %(team_leader.ky_id, event.eventName)
		
		return HttpResponse(
			json.dumps(response_data),
			content_type = "application/json"
			)
	

	membersList = []
	for Id in members:
		#print(Id)

		if Id is not '':
			try:
				kyprofile = KYProfile.objects.get(ky_id=Id)
			
				if regCheck(request, kyprofile, event):
					#print ('alreadyRe111g')
					
					response_data['status']= '%s already registered for event : %s.' %(kyprofile.ky_id, event.eventName)
					
					return HttpResponse(
						json.dumps(response_data),
						content_type = "application/json"
						)
					break;
				membersList.append(kyprofile)
				#print(membersList)
			except Exception as e:
			    # #print e
				response_data['status']='KY Id: '+Id+' is Invalid. (letters are case sensetive!)'
				#print(response_data)
				return HttpResponse(
					json.dumps(response_data),
					content_type = "application/json"
					)
	team = Team(teamName=name ,event=event,teamLeader=team_leader)
	team.save()
	team.members.add(*membersList)
	team.save()

	response_data['status'] = 'registered'
	return HttpResponse(
		json.dumps(response_data),
		content_type = "application/json"
		)	
	# 	return Response(status=status.HTTP_200_OK)
	# except Exception as e:
	# 	return Response(e)



@api_view(['POST'])
def registerIndi(request):
	post = request.data
	event_=post.get('event',0)
	team_leader=post.get('team_leader',0)
	response_data = {}
	membersList = []

	##print event_
	# try:
	kyprofile = KYProfile.objects.get(ky_id=team_leader)
	##print kyprofile
	event = Event.objects.get(eventName=event_)
	
	# except Exception as e:
	# 	response_data['error'] = str(e)
	# 	return HttpResponse(
	# 		json.dumps(response_data),
	# 		content_type = "application/json"
	# 		)
	request=None
	##print(regCheck(request,kyprofile, event))
	if not regCheck(request,kyprofile, event):
		#Team.objects.create(teamLeader=kyprofile, event = event)
		membersList.append(kyprofile)
		team = Team(event=event,teamLeader=kyprofile)
		team.save()
		team.members.add(*membersList)
		team.save()
		response_data['status'] = 'registered'
		return HttpResponse(
			json.dumps(response_data),
			content_type = "application/json"
			)
	else:
		response_data['status'] = 'already registered!'
		return HttpResponse(
			json.dumps(response_data),
			content_type = "application/json"
			)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def mobileLogin(request):
	id_ = request.data.get('ky_id', None)
	secret = request.data.get('secret', None)
	mobile_number = int(request.data.get('mobile_number', None))
	if secret == 'a23hdf348sdh34587sjhd33u98sdfh34h34g59':
		kyprofile = KYProfile.objects.filter(ky_id=id_)
		caprofile = CAProfile.objects.filter(ca_id = id_)
		if kyprofile.exists() and kyprofile[0].mobile_number == mobile_number:
			user = UserSerializer(kyprofile[0])
			print(user.data)
			return Response(user.data, status=status.HTTP_200_OK)
		elif caprofile.exists() and caprofile[0].kyprofile.mobile_number == mobile_number:
			user = UserSerializer(caprofile[0].kyprofile)
			return Response(user.data, status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_403_FORBIDDEN)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def mobileSocialLogin(request):
	email = request.data.get('email', None)
	secret = request.data.get('secret', None)
	if secret == 'a23hdf348sdh34587sjhd33u98sdfh34h34g59':
		kyprofile = KYProfile.objects.filter(email=email)
		if kyprofile.exists():
			user = UserSerializer(kyprofile[0])
			print(user.data)
			return Response(user.data, status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_403_FORBIDDEN)
	else:
		return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def mobileRegister(request): # registration with email
    post = request.data
    secret = request.data.get('secret', None)
    if secret != 'a23hdf348sdh34587sjhd33u98sdfh34h34g59':
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    email = post.get('email', None)
    name = post.get('name', None)
    password = post.get('pass1', None)
    referralCode = post.get('ref', None)
    gender = post.get('gender', None)
    collegeName = post.get('college', None)
    year = post.get('year', None)
    mobile_number = post.get('mobile_number', None)
    check_email=KYProfile.objects.filter(email=email)
    if not len(check_email):
        if collegeName and  mobile_number and year and name and password and email:
            college, created = College.objects.get_or_create(
                                            collegeName=collegeName)                                                
            kyprofile = KYProfile.objects.create(email=email,
                                                full_name=name,
                                                gender=gender,
                                                mobile_number=mobile_number,
                                                college=college,
                                                year=year,
                                                is_active=False,
                                                profile_completed=True,
                                                referralCode=referralCode)
            kyprofile.set_password(password)
            kyprofile.save()
            addKYProfileToSheet(kyprofile)
            send_reg_email(kyprofile,  get_current_site(request))                        
            return Response(status=status.HTTP_200_OK)

        else:
            return Response(user.data, status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse(status=status.HTTP_403_FORBIDDEN)
