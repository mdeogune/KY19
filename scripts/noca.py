import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'kashiyatra.settings')
django.setup()

from users.models import KYProfile, CAProfile

for kyprofile in KYProfile.objects.all().order_by('id'):
	try:
		ca = CAProfile.objects.get(kyprofile=kyprofile)
	except Exception as e:
		print(kyprofile.email, kyprofile.profile_link, '\n')
