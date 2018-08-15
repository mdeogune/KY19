#Script to update points of CAs
#python -m scripts.updatepoints
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'kashiyatra.settings')
django.setup()

from etc.models import *
from users.models import *

print('updating points \n\n')

for ca in CAProfile.objects.all():
	ca_id = ca.ca_id
	try:
		total_prs = PublicRelation.objects.filter(ca=ca).count()	
		regs = KYProfile.objects.filter(referralCode=ca_id).count()
		point = Point.objects.get(ca=ca)
		point.pr_points = 10 * total_prs
		point.reg_points = regs * 30
		point.save()
		print(ca, 'done')
	except Exception as e:
		print(e)

