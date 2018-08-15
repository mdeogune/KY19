import os
import django
import requests
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'kashiyatra.settings')
django.setup()

from users.views import addCaToSheet, addKYProfileToSheet
from users.models import KYProfile, CAProfile

for kyprofile in KYProfile.objects.all().order_by('id'):
	print(kyprofile)
	try:
		ca = CAProfile.objects.get(kyprofile=kyprofile)
		response = addCaToSheet(kyprofile, ca)
		print(response.status_code)

	except Exception as e:
		print(e)
		print(kyprofile.ky_id, kyprofile.email)
'''
for kyprofile in KYProfile.objects.all().order_by('id'):
	print(kyprofile)
	try:
		response = addKYProfileToSheet(kyprofile)
		print(response.status_code)
	except Exception as e:
		print(e)
		print(kyprofile.ky_id, kyprofile.email)
'''

for k in KYProfile.objects.filter(is_paid=True).order_by('id'):
	try:
		print(';'.join([k.ky_id, k.full_name, k.email, k.college.collegeName, str(k.year), str(k.gender), str(k.mobile_number), str(k.paid_amt), k.payment_id ]))		
	except Exception as e:
		print(e)
