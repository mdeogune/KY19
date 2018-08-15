from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView, FormView
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
import json
# import simplejson as json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site

from django.contrib.auth.models import User
from django.core.mail import EmailMessage

import requests
from allauth.socialaccount.models import SocialToken
from users.models import *
from etc.models import *
from django.utils import timezone
from kashiyatra.settings import LOGIN_URL,LOGIN_URL_social,LOGIN_URL_email
from users.apis import *


def _getNotifications(kyprofile):
    notifications = Notifications.objects.filter(users=kyprofile.caprofile,
                                                recieved_date__lte=timezone.now())
    context = {
        'notifications': notifications.order_by('recieved_date'),
        'count': notifications.count(),
    }
    return context

def IndexView(request):
    template_name = 'index.html'
    return render(request, template_name, {})

def eventRegister(request):
    template_name = 'eventsRegister.html'
    kyprofile = request.user
    if request.method == 'POST':
        post = request.POST
        event = post.get('event', None)
        member = post.get('member', None)
        regDetail=[event, member]
        event_=[]
        try:
            jsonDec = json.deco
            der.JSONDecoder()
            eventsList = jsonDec.decode(kyprofile.eventsList)
            print(eventsList.__class__)
            #print ([ _ for _ in eventsList])
            dump=[ _ for _ in eventsList]
            #for _ in eventsList:
               # event_.append( [_] )
        except Exception as e:
            pass
        #event_.append(regDetail)
        print (event_)
        kyprofile.eventsList = json.dumps( [ _ for _ in event_])
        kyprofile.save()

    return render(request, template_name, {})

def CAIndexView(request):
    template_name = 'CAIndex.html'
    return render(request, template_name, {})

@login_required(login_url=LOGIN_URL_social)
def UserFormView(request): # for completing user profile after social login
    template_name='user-form.html'
    kyprofile = request.user
    if kyprofile.profile_completed:
        return redirect('/dashboard')
    if request.method == 'POST':
        post = request.POST
        collegeName = post.get('college', None)
        year = post.get('year', None)
        mobile_number = post.get('mobile_number', None)
        referralCode = post.get('referralCode', None)

        if collegeName and  mobile_number and year:
            college, created = College.objects.get_or_create(
                                            collegeName=collegeName)                                                

            kyprofile.mobile_number = mobile_number
            kyprofile.college = college
            kyprofile.year = year
            kyprofile.referralCode = referralCode
            kyprofile.profile_completed = True
            kyprofile.save()
            return redirect('/dashboard')
        else:
            return HttpResponse("Invalid form submission")#sth to be done
    else:
        context = {
            'email': kyprofile.email,
            'full_name': kyprofile.full_name,
            'all_colleges': College.objects.all(),
        }
        return render(request, template_name, context)

@login_required(login_url=LOGIN_URL)
def CaFormView(request):#ca-form
    template_name='ca-form.html'
    kyprofile = request.user
    if request.method == 'POST':
        post = request.POST
        whatsapp_number = post.get('whatsapp_number', None)
        postal_address = post.get('postal_address', None)
        pincode = post.get('pincode', None)
        reason=post.get('reason', None)
        if  whatsapp_number and reason and postal_address and pincode :
            ca, ca_created = CAProfile.objects.get_or_create(kyprofile=kyprofile)
            ca.whatsapp_number=whatsapp_number
            ca.postal_address=postal_address
            ca.pincode=pincode
            ca.reason=reason
            ca.save()
            kyprofile.has_ca_profile = True
            kyprofile.save()
            try:
                if ca_created:
                    print('\n\n adding ca')
                    resp  = addCaToSheet(kyprofile,ca)
                    print(resp)
                    Point.objects.create(ca=ca)
                    welcome_note = Notifications.objects.all().order_by('id')[0]
                    welcome_note.users.add(ca)
                    welcome_note.save()
            except Exception as e:
                print(e)
            return redirect('/dashboard')
        else:
            return HttpResponse("Invalid form submission")#sth to be done
    else:
        context = {
            'email': kyprofile.email,
            'full_name': kyprofile.full_name,
        }
        return render(request, template_name, context)

def IncreaseRegs(ref):
    try:
        ca = CAProfile.objects.get(ca_id=ref)
        ca.reg_num +=1
        ca.save()
    except Exception as e:
        print(ref, e)

def EmailRegistration(request): # registration with email
    template_name='email_reg.html'
    if not request.user.is_authenticated():
        if request.method == 'POST':
            post = request.POST
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
                    # IncreaseRegs(referralCode) #write a script for this
                    addKYProfileToSheet(kyprofile)
                    send_reg_email(kyprofile,  get_current_site(request))                        
                    return HttpResponse('Confirmation link has been sent to your email id, Please confirm your email address to complete the registration.')

                else:
                    return HttpResponse("Invalid form submission")#sth to be done

            else:
                return HttpResponse("email already  in use!!!!!")#sth to be done

        else:
            return render(request, template_name)
    else :
        if request.user.is_active :
            return redirect('/dashboard')
        else:
            return HttpResponse('Please confirm your email address to complete the registration')

def FormView(request):
    template_name='loginmain.html'
    if not request.user.is_authenticated():
        if request.method == 'POST':
            post = request.POST
            email = post.get('email', None)
            password = post.get('pass1', None)
            print(email, password)
            if password and email:
                try:    
                    kyprofile = KYProfile.objects.get(email=email)
                except:
                    return HttpResponse('No user found')
                if not kyprofile.is_active:
                    return HttpResponse('Please confirm your account before loging in. Check your inbox for confirmation link.')
                
                kyprofile=authenticate(email=email,password=password)
                if kyprofile:
                	kyprofile.backend='django.contrib.auth.backends.ModelBackend'
                	login(request,kyprofile)
                	return redirect('/dashboard')
                else:
                	return HttpResponse('Either you have entered a wrong password or you need to try the option from which you have registered previously. (Facebook or Google)')
            else:
                return HttpResponse("Invalid form submission")#sth to be done
        else:
            return render(request, template_name)
    else:
        return redirect('/dashboard')

@login_required(login_url=LOGIN_URL)
def DashboardView(request):
    kyprofile = request.user
    print(kyprofile.profile_completed, kyprofile.has_ca_profile)
    if kyprofile.profile_completed:
        if kyprofile.has_ca_profile:
            template_name = 'angular/ca/index.html'
        else:
            template_name = 'angular/user/index.html'
        return render(request, template_name, {})
    else:
        return redirect('/user-form')

def PrivacyPolicyView(request):
    template_name = 'privacy_policy.html'
    return render(request, template_name, {})

def LogoutView(request):
    logout(request)
    return redirect('/')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = KYProfile.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        print(e)
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return redirect('/dashboard')
    else:
        return HttpResponse('Activation link is invalid!')

@csrf_exempt
def reset_(request, uidb64, token):
    
    if request.method == 'GET':
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = KYProfile.objects.get(pk=uid)
            return render(request,"reset.html")
        except:
            user = None
            
            return redirect('/form')
    elif request.method == "POST":
        post = request.POST
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = KYProfile.objects.get(pk=uid)
            
            password1 = post.get('password1')
            password2 = post.get('password2')
            if password1 == password2:
                user.set_password(password1)
                user.save()
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                messages.success(request,'password set successfully!',fail_silently=True)
                return redirect('/dashboard')
            else:
                messages.warning(request, "passwords didn't match!")
                
                
        except Exception as e:
            return HttpResponse(e)
    # if user is not None and account_activation_token.check_token(user, token):
    #     user.is_active = True
    #     user.save()
    #     user.backend = 'django.contrib.auth.backends.ModelBackend'
    #     login(request, user)
    #     return redirect('/dashboard')
    # else:
    # return HttpResponse('Activation link is invalid!')



@csrf_exempt
def forgotPassword(request):
    if request.user.is_authenticated():
        return redirect('/dashboard')
    if request.method == 'POST':
        email = request.POST.get("email")
        try:
            kyprofile = KYProfile.objects.get(email = email)
            # if user.is_active is False:
            #     messages.warning(request,"Please confirm your email first!")
            #     return redirect('/login')
        except:
            messages.warning(request, "Invalid Email!")
            return redirect('/forgotPass')

        send_reset_pass(kyprofile,  get_current_site(request))
        messages.success(request, "Password Reset link sent to your Email.")
        return redirect('/forgotPass')
        # subject = "Reset Password"
        # forgotPassKey = 'asljdkflasjkdf' + email + 'jalfdjskdjf'
        # forgotPassKey = str(hash(forgotPassKey))
        # try:
        #     key = Key.objects.get(kyprofile = user.kyprofile)
        #     key.forgotPassKey = forgotPassKey
        #     key.save()
        # except:
        #     key = Key(kyprofile = user.kyprofile, forgotPassKey = forgotPassKey)
        #     key.save()

        # body = "Please Cick on the following link to reset your Password for Kashiyatra'17.\n\n"
        # body += server + "resetPass/" + forgotPassKey
        # try:
        #     if send_email(subject, body, email):
        #         messages.success(request, "Password Reset link sent to your Email.")
        #         return redirect('/form')
        # except:
        #     messages.warning(request, "Email couldn't  be send, Retry please!")
        #     return redirect('/forgotPass')
    elif request.method == 'GET':
        return render(request,'forgotpass.html', {})
    # else:
    #     raise Http404('NOT ALLOWED')