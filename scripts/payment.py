import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'kashiyatra.settings')
django.setup()


from users.models import *
kys = KYProfile.objects.filter(is_paid=True)
c = 0
for p in kys:
	c += 1
	try:
		i = p.caprofile.ca_id
	except:
		i = "None"
	print(";".join(map(str, [c, p.ky_id, i, p.full_name, p.college.collegeName, p.mobile_number, p.paid_amt])))
