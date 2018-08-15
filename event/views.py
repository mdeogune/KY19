from django.shortcuts import render,HttpResponseRedirect,redirect,Http404, HttpResponse, render_to_response
from django.contrib.auth import authenticate, login, logout
#from KYusers.emailBackend import LoginUsingEmailAsUsernameBackend
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages
from django.contrib.messages import get_messages

from django.contrib.auth.decorators import login_required
from users.models import *
from event.models import *
from users.forms import *
from kashiyatra.settings import LOGIN_URL,LOGIN_URL_social,LOGIN_URL_email
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives

# @login_required(login_url = LOGIN_URL)
def eventPage(request):
    template_name = 'events/index.html'
    return render(request, template_name, {})

def eventCatPage(request, eventCatName):
    try:
        template_name = 'events/%s.html' % eventCatName
        get_template(template_name)
    except:
        raise Http404('Page not found')
        
    parentevent = ParentEvent.objects.get(categoryName=eventCatName.upper())
    context = {
    'events' : Event.objects.filter(parentEvent=parentevent),
    }
    print(context)
    return render(request, template_name, context)


def regCheck(request, kyprofile, event):
    print ('checking ', kyprofile)
    alreadyReg = False
    try:
        Team.objects.get(event=event, teamLeader=kyprofile)
        alreadyReg = True
    except:# not a team leader
        try:
            Team.objects.get(event=event, members=kyprofile)
            alreadyReg = True
        except:#not reg as team member too
            pass

    if alreadyReg:
        print ('alreadyReg')
        try:
            messages.info(request, '%s already registered for event : %s.' %(kyprofile.kyId, event.eventName), fail_silently=True)
        except:
            pass
    return alreadyReg


@login_required(login_url = LOGIN_URL)
def eventRegistration(request, eventName):
    event = Event.objects.get(eventName=eventName)
    template_name = 'eventRegister.html'
    context = {
        'event':event,
    }
    kyprofile = request.user
    
    regCheck(request, kyprofile, event)

    if request.method == "POST":

        post = request.POST
        print (post)
        teamName = post['teamName']
        leaderId = post['leader']
        memberIds = post.getlist("fields[]")
        try:
            teamLeader = KYProfile.objects.get(kyId = leaderId)
            regCheck(request, teamLeader, event)
        except Exception as e:
            messages.error(request, 'Team Leader\'s KY Id: %s is Invalid. (letters are case sensetive!)' %leaderId, fail_silently=True)
            return render(request, template_name, context)
        team = Team(teamName=teamName, event=event, teamLeader=teamLeader)
        membersList = []
        for Id in memberIds:
            if Id is not '':
                try:
                    kyprofile = KYProfile.objects.get(ky_id=Id)
                    regCheck(request, kyprofile, event)
                    membersList.append(kyprofile)
                except Exception as e:
                    # print e
                    messages.error(request, 'KY Id: %s is Invalid. (letters are case sensetive!)', fail_silently=True)
                    return render(request, template_name, context)

        msg = messages.get_messages(request)
        if msg:
            print (msg)
            return render(request, template_name,context)

        team.save()
        team.members.add(*membersList)
        team.save()

        messages.success(request, 'Registration for %s successfull!' %(eventName), fail_silently=True)
        return render(request, template_name, context)
    else:
        return render(request,template_name, context)





def individualReg(request):
    print("56565")
    if request.method == "POST":
        response_data = {}
        kyId = request.POST.get('ky_id')
        print(kyId)
        eventId = request.POST.get('eventId')
        print(eventId)
        try:
            kyprofile = KYProfile.objects.get(ky_id=kyId)
            print (kyprofile)
            event = Event.objects.get(eventId=eventId)
            print (event)
        except Exception as e:
            response_data['error'] = str(e)
            return HttpResponse(
                json.dumps(response_data),
                content_type = "application/json"
                )
        request=None
        print(regCheck(request,kyprofile, event))
        if not regCheck(request,kyprofile, event):
            Team.objects.create(teamLeader=kyprofile, event = event)
            response_data['status'] = 'registered'
            return HttpResponse(
                json.dumps(response_data),
                content_type = "application/json"
                )
        else:
            return HttpResponse('already registered!')
    else:
        return HttpResponse('not allowed')


def regCheckAjax(request):
    if request.method == "POST":
        response_data = {}
        kyId = request.POST.get('kyId')
        eventId = request.POST.get('eventId')
        kyprofile = KYProfile.objects.get(kyId=kyId)
        event = Event.objects.get(eventId=eventId)
        request = None
        if regCheck(request,kyprofile, event):
            response_data['status'] = 'registered'
        else:
            response_data['status'] = 'not_registered'

        return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
    else:
        return HttpResponse('not allowed')