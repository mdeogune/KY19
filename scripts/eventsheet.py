'''
Updates event sheet.
checkpoint.csv contains the last team which was added to the sheet. 
'''
import os
import django
import requests
import csv
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'kashiyatra.settings')
django.setup()

from event.models import Team

def EventSheetUpdate(team):
    dic = {
    'eventName' : team.event.eventName,
    'teamName' : team.teamName,
    'teamLeader' : [str(team.teamLeader.full_name)+" "+str(team.teamLeader.ky_id)],
    'college': team.teamLeader.college.collegeName,
    'members' : str([str(x.full_name) + " : " + str(x.ky_id) for x in team.members.all()]),
    'memNum': len(team.members.all()),
    'parentEvent' : team.event.parentEvent.categoryName,
    }
    url = "https://script.google.com/a/itbhu.ac.in/macros/s/AKfycbywC5S-LFfaXrVcI4CpGOMVaNoLrjCuabrMnt3Ayanyk7K6pkg/exec"
    try:        
        resp = requests.post(url,data=dic)
        print(resp.status_code, team.teamId)
    except requests.exceptions.ConnectionError:
        print ('ConnectionError')

if __name__=='main':
	with open('scripts/checkpoint.csv','r') as f:
		data = csv.reader(f)
		for row in data:
			print(row)
			if row[0] == 'TeamId':
				baseTeamId = row[1]
				break

	for team in Team.objects.filter(teamId__gte=553).order_by('teamId'):
		EventSheetUpdate(team)
		# newBaseTeamId = team.teamId


	with open('scripts/checkpoint.csv','w') as f:
		writer = csv.writer(f)
		writer.writerow(['TeamId', newBaseTeamId])

	print("newBaseTeamId", newBaseTeamId)

