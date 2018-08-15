import sendgrid
import os
from sendgrid.helpers.mail import *
import csv

import django
from django.core.mail import EmailMultiAlternatives

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'kashiyatra.settings')
django.setup()

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('sgkey'))
i = 1
subject = "Greetings from Kashiyatra 2018"
with open('scripts/camails.csv') as f:
	data = csv.reader(f)
	for row in data:
		ca_id = row[0]
		name = row[1]
		email = row[2]
		print(i, ca_id, name, email)
		body = '''Greetings from Team Kashiyatra!!
			 
			Congratulations {0}! You have been selected as the Campus Ambassador of Kashiyatra’18. Welcome to the team! Your Referral ID is {1}.
			 
			Kashiyatra, the cultural extravaganza of Indian Institute Of Technology (Banaras Hindu University), Varanasi, is one of the biggest galas of North India. Hosted in the heart of the cultural capital of the country, Banaras, Kashiyatra attracts a swarm of talents from across the nation, in a magnificent display of flair, flamboyance and panache.

			We hereby take immense pleasure in informing you that the 36th Edition of KY is to be held from 19th-21st January, 2018, in the heart of the cultural richness of Banaras.

			Here is a new task for you guys. We want you to provide us with the contact details of the following people, it is mandatory. The more the contacts you provide, the more points you will be receiving.
			·        Cultural Head of your college

			·        Cultural Festival Head of your college

			·        Dramatics Head/Streetplay Head of your college

			·        Dance Head of your college

			·        Theatre Head of your college

			·        Music Head of your college

			·        Fine Arts Head of your college

			·        Literary Head of your college

			_____

			For accomplishing the duties of a Campus Ambassador, we expect you to complete the task given in stipulated time. You will be sharing these details from the CA Portal, under the Public Relations tab.

			Kashiyatra promises to be an experience unlike any other and we look forward to seeing you and your friends at our fest.

			P.S.
			1: Please find the attachments:
				 Information Brochure: https://drive.google.com/file/d/0B9X3w1E0dbavSjV0VVV5aFYzdFU/view
				 Campus Ambassador Guidelines: https://drive.google.com/file/d/0B9X3w1E0dbavZjFYdEFEa25pb1U/view
				 Events Poster: https://drive.google.com/file/d/0B9X3w1E0dbavSTVnY0dHSy11Qkk/view

			2: Get in touch with undersigned people via WhatsApp or Facebook for further instructions.

			Sai Sumanth: +91-9493690659
			Email ID: sumanth@kashiyatra.org

			Kalpesh Bansal: +91-7233013288
			Email ID: kalpesh@kashiyatra.org


			Cheers!
			Team KY
			http://www.kashiyatra.org
			
			Visit us at:

			Facebook: https://www.facebook.com/kashiyatra.IITBHU

			Instagram: https://www.instagram.com/kashiyatra_iitbhu

			Twitter: https://twitter.com/KY_IITBHU

			Youtube: https://www.youtube.com/kashiyatraiitbhu


			'''.format(name, ca_id)
		# print(body)
		mail = EmailMultiAlternatives(
		  subject = subject,
		  body = body,
		  from_email = "Kashiyatra Indian Institute of Technology (BHU) Varanasi <kashiyatra@iitbhu.ac.in>",
		  to = [email],
		  reply_to = ["kashiyatra@iitbhu.ac.in"],
		)
		# mail.attach_file('/media/ags/DATA/CODE/WEB/KY/2018/KY18/scripts/Campus Ambassador Guidelines.pdf')
		# mail.attach_file('/media/ags/DATA/CODE/WEB/KY/2018/KY18/scripts/Events Poster.jpg')
		# mail.attach_file('/media/ags/DATA/CODE/WEB/KY/2018/KY18/scripts/Information Brochure.pdf')
		try:
			mail.send()
		except Exception as e:
			print(e)
		i+=1