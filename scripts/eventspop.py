import os
import django
import requests
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'kashiyatra.settings')
django.setup()

from users.models import KYProfile
from event.models import ParentEvent, Event


CategoryList = [['NATRAJ',
                  ['BLISS', 5, 35], ['CUT-A-RUG', 1, 1], ['ECSTASY', 2, 2], ['NRITYA', 4, 12]],
                ['ABHINAY',
                 ['RANGMANCH', 1, 12], ['ASMITA', 1, 1], ['HULLAD', 10, 30]],
                ['CROSSWINDZ',
                 ['BATTLE OF BANDS', 3, 20], ['INSTRIMENTAL SHOWDOWN', 3, 20 ]], #NO MAX LIMIT
                ['BANDISH',
                 ['SUR', 1, 1], ['SARGAM', 6, 15], ['SANLAYAN', 1, 1], ['KRITI', 1, 20], ['ADVAITA', 3, 10]],
                ['MIRAGE',
                 ['DESIGN ELEGANTE', 8, 20], ['MR. KY', 1, 1], ['MISS KY', 1, 1]],
                ['TOOLIKA',
                 ['RAPID FIRE', 4, 4], ['SPOIL THE TEES!', 1, 3], ['LIVE SKETCHING', 1, 2], ['VASTRA SHILP', 1, 4],
                 ['RANGBAAZI', 1, 2], ['CLAY MODELLING', 1, 4], ['SOAP CARVING', 1, 2]],
                ['ENQUIZTA',
                 ['INDIA QUIZ', 1, 3],['MELA', 1, 3], ['GENERAL QUIZ', 1, 3],['SPORTS QUIZ', 1, 3],['BIZ TECH QUIZ', 1, 3]],
                ['SAMWAAD',
                 ['SCRIPTURESQUE', 1, 1], ['BATTLEFRONT', 1, 1], ['SHIPWRECK COVE', 1, 1], 
                 ['THE LEGEND OF SIR SPEAK-A-LOT', 1, 1], ['A JESTERS COURT', 1, 1], ["WHAT'S THE WORD?", 2, 2],
                  ['VAAD VIVAAD', 1, 1], ['ALFAAZ', 1, 1], ['ASHUBHASHAN', 1, 1 ]],
                ['XTASY',
                 ['INK IT',1, 2], ['THIRD EYE', 1, 5], ['FX MAKEUP', 1, 3]],
]
for i in CategoryList:
    print (i[0], '\n')
    parentevent = ParentEvent.objects.create(categoryName=i[0])
    for j in i[1:]:
        print(j)
        Event.objects.create(eventName=j[0], parentEvent=parentevent, minMembers=j[1], maxMembers=j[2])
    print ('done!')