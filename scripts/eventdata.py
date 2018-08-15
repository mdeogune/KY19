import os
import django
import requests
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'kashiyatra.settings')
django.setup()

from users.models import KYProfile
from event.models import ParentEvent, Event

EventData = {}

EventData['BLISS'] = '''
Preliminary Round <br><br>
Time limit: 3-5 minutes. Exceeding this will lead to penalization in marks.
Team size: Minimum of 5 and maximum of 35 members are allowed in a team,
with at least 3 and at most 20 members on stage at any point during the
performance.<br><br>
1. All dance forms except folk are allowed.<br>
2. Participants can use props suited to their performance. Props which might
cause inconvenience to the other teams or cause damage to the stage or the
surroundings, will not be entertained under any circumstance (this applies to
any kind of fluid, flame, powders, colours, confetti, glass etc.).<br>
3. The performance must be a part of the routine that is to be presented in the
final round.<br>
4. Participants are required to give the corresponding edited audio songs of
both the rounds in .mp3 format, in PENDRIVES ONLY and must be submitted at
the time of registration. Others devices such as CDs or mobile phones etc will
not be accepted.<br>
5. Decision of the judges and the coordinators will be considered as final and
binding and will not be changed under any circumstances.<br>

6. Obscenity of any kind will lead to immediate disqualification.<br><br>

Final Round <br><br>

Stage setting time: 2 minutes (maximum).<br>

Time limit: 6-10 minutes. Exceeding this will lead to penalization in marks.<br>

1. Participants can use props suited to their performance.<br>

2. Participants are required to give the corresponding edited audio songs in
.mp3 format, in PENDRIVES ONLY along with the final round track and must be
submitted at the time of registration.<br>
3. No substitutions are allowed. Only the same team that was registered for the
eliminations will be allowed to perform in the finals if it qualifies. <br>
4. Any specific requirements regarding lights and smoke must be discussed with
organizers well in advance.<br>
[NOTE: The pendrive must contain two tracks, one for preliminary round and
the other for final. Named as: BLISS – your group name/college nameround(PRELIMS/FINAL),
e.g. : BLISS-IITBHU-PRELIMS indicates IITBHU’s track for
PRELIMINARY round].<br>
'''

EventData['CUT-A-RUG'] = '''

1. All dance forms are allowed. <br>
2. There will be three rounds present in the competition.<br>
3. In the first round, participants will perform for not more than 1 minute. The
performance must be a part of the routine that is to be presented in the second
round.<br>
4. In the second round, participants will have 4 minutes (maximum) to perform.<br>
5. The final round will be a one-on-one face-off competition in which the
finalists will perform on the spot to a music piece selected randomly which will
be given to the participant 5 minutes before their performance.<br><br>
6. Participants can use props suited to their performance. Use of any kind of
fluid, flame, powders, glass and colours is not allowed.<br>
7. Participants are required to give the corresponding edited audio songs in
.mp3 format, in PENDRIVES ONLY along and must be submitted at the time of
registration. Others devices such as CDs or mobile phones etc. will not be
accepted.<br>
8. Decision of the judges and the coordinators will be considered as final and
binding and will not be changed under any circumstance.<br>
[NOTE: The pendrive must contain two tracks, one for first round and the other
for second. Named as: CAR-your_name-round_name (PRELIMS/FINAL)
e.g.: CAR-P_Ashutosh-PRELIMS indicates P.Ashutosh’s track for PRELIMINARY
round].<br>
'''

EventData['ECSTASY'] = '''
Preliminary Round<br><br>
Time limit: 2 minutes. Exceeding this will lead to penalization in marks.<br>
1. All dance forms are allowed.<br>
2. There is no gender restriction.<br>
3. Participants can use props suited to their performance. Props which might
cause inconvenience to the other teams or cause damage to the stage or the
surroundings, will not be entertained under any circumstance (this applies to
any kind of fluid, flame, powders, colours, confetti, glass etc.).<br>
4. Participants are required to give the corresponding edited audio songs of
both the rounds in .mp3 format, in PENDRIVES ONLY and must be submitted at
the time of registration.<br>
5. Decision of the judges and the coordinators will be considered as final and
binding and will not be changed under any circumstances.<br><br>
Final Round<br><br>
Time limit: 5 minutes. Exceeding this will lead to penalization in marks.
1. Use of water, fire and glass is prohibited.<br>
2. Participants are required to give the corresponding edited audio songs of
both the rounds in .mp3 format, in PENDRIVES ONLY and must be submitted at
the time of registration.<br>
3. Any specific requirements regarding lights and smoke must be discussed with
organizers well in advance.<br>
[NOTE: The pendrive must contain two tracks, one for preliminary round & the
other for final. Named: ECS - participants_name-round (PRELIMS/ FINAL),
e.g.: ECS- John, Jane-FINAL indicates John & Jane’s track for FINAL round].<br>

'''

EventData['NRITYA'] = '''
Stage setting time: 2 minutes (maximum)<br><br>
Time limit: 4-7 minutes. Exceeding this will lead to penalization in marks.<br>
Team size: Minimum of 4 and maximum of 12 members are allowed in the
contingent.<br><br>
1. Songs must be purely folk. Strictly no Bollywood songs are allowed.<br>
2. Fusion of 2 or more dance styles is not allowed.<br>
3. Costumes and props will be included in the judging criteria.<br>
4. Props which might cause inconvenience to the other teams or cause damage
to the stage or the surroundings, will not be entertained under any
circumstance (this applies to any kind of fluid, flame, powders, colours, confetti,
glass etc.).<br>
5. Decision of the judges and the coordinators will be considered as final and
binding and will not be changed under any circumstances.<br>
6. Participants are required to give the corresponding edited audio songs in
.mp3 format, in PENDRIVES ONLY and must be submitted at the time of
registration. Others devices such as CDs or mobile phones etc. will not be
accepted.<br>
7. Performers are required to clear the stage after the performance otherwise
they will be penalized.<br><br>
[NOTE: The pendrive must contain the track. Named as:
NRI-your_name
e.g.: NRI-P_Ashutosh indicates P.Ashutosh’s track ].

'''

EventData['RANGMANCH'] = '''
1. Length of the play should be around 20 to 50 minutes, with a penalty for
every extra minute. An extra time of 5 minutes will be given both for setting as
well as clearing the stage.<br>
2. A technical check (both lights and sound) will be provided to each team
before the starting of the event.<br>
3. Play could be in English, Hindi or Bilingual. Short phrases of other languages
can be used.<br>
4. There is no restriction to team size but the stage limit is restricted to a
maximum of 12 actors.<br>
5. Teams are allowed to have one member each for lights, sound and spot. In
addition to that a maximum of three backstage helpers are allowed. Their
names should be mentioned separately at the time of Registration.<br>
6. Any type of Inappropriate content or vulgarity will not be tolerated.
7. Stage Props should be mentioned beforehand and can be used only after the
consent of the Coordinating Team.<br>
8. The decision of the organizers shall be final and abiding.<br>
9. Slot preference will be given in the order of registration on the first come first
serve basis.<br>

'''


EventData['ASMITA'] = '''
1. A participant can have a maximum of 3 helpers, one each for lights and sound
and the third one could be incorporated in the act as per need.<br>
2. Act can be in English, Hindi or Bilingual. Short phrases of other languages can
be used.<br>
3. Time Limit: 4-10 minutes.<br>
4. Any kind of Fluid, live animals, flames, heavy objects or any material which
has a possibility of damaging the stage is not allowed.<br>
5. Points will be deducted on exceeding the time limit.<br>
6. Any type of Inappropriate content or vulgarity will not be tolerated.<br>
7. Stage Props should be mentioned beforehand and can be used only after the
consent of the Coordinating Team.<br>
8. The decision of the judges and organizers shall be final and abiding. <br>
'''

EventData['HULLAD'] = '''
1. Team Size: 10-30 (including CAs & music accompanists)<br>
2. Teams have to mail the following things at events.kashiyatra@gmail.com :<br>
Synopsis of the play (not more than 100 words) and Prod List (List of production
material and music instruments brought by the teams). The subject of the email
should be “College Name_Play Name” before the mentioned deadline.<br>
3. Time Limit: 15-30 minutes. Points will be deducted on exceeding the time
limit.<br>
4. Judging Criteria: Acting, Voice (Sync, modulation and diction) Screenplay,
Script, Audience Interaction & overall impact.<br>
5. The team size represents the number of people registered as a team. Only
these shall be allowed to perform the Street play.<br>
6. Music accompanists are included in the team number stated above.
Maximum of 4 can be included in the team.<br>
7. Teams are expected to perform at an open air venue with audience all
around.<br>
8. No electrical appliances shall be allowed during the performance whether
inside or outside the circle of performance.<br>
9. Only live music is allowed. Teams will have to bring their own instruments. No
instruments will be provided.<br>
10. Language of the performance should be Hindi/English or both. However,
short sub passages in other languages are allowed.<br>
11. Any kind of Fluid, live animals, flames, heavy objects or any material which
has a possibility of damaging the stage is not allowed.<br>
12. Dry colours may be used during the play, but the teams have to clean the
stage after their performance & the cleaning time will be included in the
performance time.<br>
13. Any kind of plagiarism & profanity will lead to immediate disqualification.<br>
14. The decision of the judges and organizers will be final & abiding. <br>
'''

EventData['BATTLE OF BANDS'] = '''
The competition will be held in two phases, zonals in various cities and the
finals in Varanasi.<br><br>
Rules for zonal: (subject to change as per venue)<br><br>
1. The competition is open for all English semi-professional bands having atleast
one original composition.<br>
2. Each band would be given a playing time of 20 minutes, inclusive of sound
set-up.<br>
3. Basic sound equipment and a standard drum-kit will be provided, bands are
however advised to bring their own guitars, keyboards, and additional
equipment.<br>
4. There is no upper-limit for the number of members in a band, however at
any point of time at least three members need to be on the stage.<br>
5. No pre-recorded audio or MIDI interfaces are allowed. However bands
can use looper pedals for live loopings.<br>
6. All songs much have their lyrics written in English.<br>
7. The judge’s decision will be final.<br>
8. Based on the participation, we will select a maximum of two bands who
will advance for the finals in Varanasi.<br><br>
Rules for final:<br><br>
1. Varanasi zonals will be held during Kashiyatra. The bands which have
already participated in any other zonals can also participate in the Varanasi
Zonals.<br>
2. The finals will be held in Varanasi during Kashiyatra. All the bands have to
arrange their travel up to Varanasi.<br>
3. Bands will be given 15 minutes time before their performances for sound
setup. They can save the patches at that moment for their performances.<br>
4. The performance time is limited to 20 minutes per band. The
performances will be right before the headlining act by Guest Bands.<br>
5. No pre-recorded audio or MIDI interfaces are allowed. However bands
can use looper pedals for live loopings.<br>
6. All songs much have their lyrics written in English.<br>
7. The judge’s decision will be final, the results would be announced by the
judges right after the headlining act of that day.<br>
8. Any change in the above rules will be notified to the concerned bands
prior to their performances.<br><br>
Prizes:<br><br>
1. Zonal winners will get free accommodation during the duration of the
fest in Varanasi.<br>
2. There will be prizes to the best band and the runners-up band which will
a significant cash amount.<br>
3. There will also be attractive prizes for the best Guitarist, best Drummer,
best Vocalist.<br>
'''

EventData['SUR'] = '''
1. Time limit:<br>
• Prelims- 3 minutes including sound-check.<br>
• Finale- 6 minutes including sound-check.<br>
2. Genre: Classical songs are NOT allowed. However, Semi-classical, Light Indian
Music, Bollywood and Western songs (NO screaming/ growling) are allowed.
3. Language: All languages are allowed.<br>
4. Background tracks are permitted. Participants will have to carry it in a
pendrive and the submission of the track should be done prior to the event.
5. You may be asked to sing another song on judge’s demand.<br>
6. Mashups and Medleys are allowed, provided they don’t exceed the time
limit.<br>
7. You may bring along two accompanying instrumentalists with you, or may
play the instrument yourself, or use an Electronic Tanpura (under either case,
you can’t use more than two instruments.). Only vocals shall be judged,
however.<br>
8. Judging Criteria: Voice Quality, Voice Modulation, Sur, Taal and Choice of
Song.<br>
9. Points may be deducted on exceeding the time limit.<br>
10. You have to perform a different composition in the finale of the event.<br>
11. The decision of the judges and the organizers will be final & abiding. <br>


'''


EventData['SARGAM'] = '''
1. Time limit: 10 minutes including sound check.<br>
2. The group should be of a minimum of 6 and a maximum of 15 participants.<br>
3. The minimum number of vocalists in the group should be 4 and the
maximum number of instrumentalists in the group should be 3.<br>
4. The instrumentalists and the vocalists are both counted as team members.<br>
5. Members singing and playing an instrument simultaneously will be counted
as two.<br>
6. The team may sing more than one song within the time limit.<br>
7. The songs must be in either English, Hindi or any Indian regional language.<br>
8. Please check the availability of the instruments with the organizing team
prior to the event. In case of non-availability, you will have to arrange the
instruments on your own.<br>
9. There will be only a single round.<br>
10. Judging Criteria: Coordination, Sur and Taal, Vocal, Public Appeal and Overall
Performance.<br>
11. The decision of the judges and the organizers will be final & abiding.<br>


'''

EventData['SANLAYAN'] = '''
Prelims<br><br>
1. Time limit: 6 minutes including sound check.<br>
2. Genre: All genres are accepted.<br>
3. Backing tracks are not allowed but music can be looped in real time.<br>
4. Judging Criteria: Clarity of Rendition, Creativity, Proficiency and level of
difficulty of composition. Original pieces will be given due weightage.<br>
5. Points may be deducted on exceeding the time limit or in case of using the
aid of written notations.<br>
6. All Instruments (String, Wind, Percussion-Electronic as well as Acoustic) are
allowed.<br>
7. The participants will be judged in 2 separate categories :
Percussion and non percussion.<br>
8. The decision of the judges and the organizers will be final & abiding.<br><br>


Final Round<br><br>
1. Selected participants from the prelims will go into the final round.<br>
2. General rules will remain same as the prelims.<br>
3. In the final round, for the percussion category, each selected participant will
be given a melody/baseline on the spot, to play on.<br>
4. For the non-percussion category, each selected participant will be given a
drum beat on the spot, to play on.<br>
5. All the participants are required to play and improvise on the given track.<br>
6. The decision of the judges and the organizers will be final & abiding.<br>


'''

EventData['KRITI'] = '''

1. Time Limit:- 8 minutes (including sound check)<br>
2. You can perform only one composition.<br>
3. Your song should be self written and self composed.<br>
4. Genre: Classical songs are NOT allowed. However, Semi-classical, Light Indian
Music, Bollywood and Western songs (NO screaming/ growling) are allowed.<br>
5. Your song can be a pure instrumental composition however song with lyrics
will be preferred.<br>
6. You can repeat the same composition performed in Kriti as in any of the
other events of the Bandish.<br>
7. If your song contains lyrics printed copies of the same should be brought at
the time of the event.<br>
8. Judging Criteria: Originality of ideas, Creativity, Composition, Arrangement of
the song, Sur, Lyrical Content, Taal and Voice quality.<br>
9. Plagiarism of any kind will be detrimental to one’s score.<br>
10. Point may be deducted on exceeding the time limit or in case of not
memorizing the lyrics (Vocalisits) or using written notations (Instrumentalists).<br>
11. The decision of the judges and the organizers will be final & abiding<br>

'''


EventData['ADVAITA'] = '''
1. Time limit: 25 minutes including sound check.<br>
2. Your performance may be of any genre and language.<br>
3. Mashups and Medleys are allowed, provided they don’t exceed the time
limit.<br>
4. Number of band members should not fall below 3 and should not exceed 10.<br>
5. Obscenity and vulgarity is not allowed in lyrics and gestures.<br>
6. No pre recorded music is allowed. Although music can be looped in real time.<br>
7. You may use as many instruments as you wish. Please check the availability<br>
of the instrument with the organizing team prior to the event. In case of nonavailability,
you will have to arrange the instruments on your own.<br>
8. For preliminary round, you have to mail your video to:
events.kashiyatra@gmail.com<br>
9. Judging Criteria: Instrumental Brilliance, Creativity, Stage Presence, Tightness,
Vocals and Public Appeal.<br>
10. Points may be deducted on exceeding the time limit or in case of not
memorizing the lyrics (vocalists) or using the aid of written notations
(instrumentalists).<br>
11. The decision of the judges and the organizers will be final & abiding.<br>


'''



EventData['DESIGN ELEGANTE'] = '''

1. This is a Designer event. There is no limit on the number of designers in the
team. They are supposed to represent their designs through models.<br>
2. A team should consist of a minimum of 8 models (apart from designers). The
team members can be from the same or different institution.<br>
3. Each team will have to choose a theme and costumes/dresses should be
centred on the chosen theme. There is no restriction on the theme and you can
freely make use of any means to choose one.<br>
Below are some of the suggested ones:<br>
a. Any Indian Mythology (Maheshmati, Bajirao Mastani, Jodha Akbar)<br>
b. Ethnic<br>
c. Shahi Libaaz<br>
d. Game of Thrones<br>
e. Being Banarasi<br>
f. Evening Gown<br>
g. Haunted House<br>
4. The participating teams will have to get themselves registered for
participation either online or on-the-spot.<br>
5. Participating teams will have to submit a written document which should
contain a summary of the theme elaborating the relation of their dress
collection to the chosen theme, formation and music for walk, prior to the
event. For online registrations, register on Kashiyatra's website first and then
email your document to: events.kashiyatra@gmail.com . For on-the-spot
registrations, document has to be submitted in hard-copy at the registration
desk.<br>
6. There will be two rounds - Prelims and Finals.<br>
7. For prelims each team will be allotted a time slot of 4-6 minutes for the
onstage performance. Exceeding the time will lead to penalization.<br>
8. For finals each team will be allotted a time slot of 8-10 minutes for the
onstage performance. Exceeding the time will lead to penalization.<br>
9. Teams are suggested to inform the organizers of any kind of props they are
planning to use. Use of water, fire, pets or any hazardous materials is not
allowed. Teams are instructed to consult with the organizers before using any
such material.<br>
10. Teams will have to bring their own music for the walk.<br>
11. The teams will be judged on the following basis:<br>
 Formation on the stage<br>
 Music<br>
 Walk<br>
 Design of the dress<br>
 Handout submitted at the time of registration which should contain the
summary of the theme elaborating the relation of their dress collection to
the chosen theme, formation and music for walk.<br>
 On-the-spot portrayal of the dresses. Failure in portraying the chosen
theme will lead to negative points.<br>
12. The decision of the judges will be final & abiding.<br>
13. Obscenity of any kind is not allowed and will lead to immediate
disqualification.<br>
'''



EventData['MR. KY'] = '''
1. This is an individual competition. Participants should get themselves
registered for participation either online or on-the-spot.<br>
2. There will be 2 rounds. They will include:<br><br>
a. Dress and Walk<br>
-The participants need to showcase their talent by carrying their dresses
elegantly and walking just like a King on the red carpet.<br>
-Individuals are free to choose the style of their outfits.<br>
-The participants should get music (if needed) in pen-drive and submit it to
the organizing team before the beginning of the event.<br>
b. Questionnaire Round<br>
The Participants would need to impress the judges with out of the box
answers to their questions.<br><br>
3. Participants will be judged on their ability to project their personality and
project his views.<br>
4. The decision of the judges and organizers will be final & abiding.<br>
5. Obscenity of any kind is not allowed and will lead to immediate
disqualification<br>


'''



EventData['MISS KY'] = '''
1. This is an individual competition. Participants should get themselves
registered for participation either online or on-the-spot.<br>
2. There will be 2 rounds. They will include:<br>
a. Dress and Walk<br>
-The participants need to showcase their talent by carrying their dresses
elegantly and walking.<br>
-Individuals are free to choose the style of their outfits.<br>
-The participants should get music (if needed) in pen-drive and submit it to
the organizing team before the beginning of the event.<br>
b. Questionnaire Round<br>
The Participants would need to impress the judges with out of the box
answers to their questions.<br>
3. Participants will be judged on their ability to project their personality and
project her views.<br>
4. The decision of the judges will be final & abiding.<br>
5. Kashiyatra reserves the right to disqualify a participant at any point in the
procedure.<br>


'''



EventData['RAPID FIRE'] = '''
Time limit: 4 hours<br><br>
1. Three contests to be completed within given time frame.<br>
2. The contests and time limit to be declared on the spot.<br>
3. Participants need to participate in teams of four.<br>
4 . All materials will be provided on the spot.<br>
5. Judging Criteria: Creativity, Neatness, Relevance to the theme, Artistic skills
and Overall appeal.<br>
6. The decision of the judges will be final & abiding
<br>

'''

EventData['SPOIL THE TEES!'] = '''
Time limit: 3 hours<br><br>
1. Teams of maximum three members.<br>
2. The theme will be given on the spot.<br>
3. Fabric colour, T-shirts, brushes, etc. will be provided.<br>
4. No additional materials are allowed.<br>
5. Judging Criteria: Creativity, Relevance to the theme, Wear-ability, Visual
appeal.<br>
6. The decision of the judges will be final & abiding<br>
'''


EventData['LIVE SKETCHING'] = '''
Time limit - 2 Days<br>
1. Teams of maximum two members.<br>
2. A4 sheets, pencils, etc. will be provided.<br>
3. No additional materials are allowed.<br>
4. Judging Criteria: Creativity, Neatness, Artistic touch, uniqueness.<br>
5. The decision of the judges will be final & abiding.<br>
'''


EventData['VASTRA SHILP'] = '''
Time limit: 3 hours.<br>
1. Teams of maximum four members.<br>
2. The theme will be given on the spot.<br>
3. All the relevant materials (coloured sheets, Fevicol, etc.) will be provided.<br>
4. No other material is allowed.<br>
5. Judging Criteria: Creativity, Relevance to the theme, Uniqueness, Finishing,
Style.<br>
6. The decision of the judges will be final & abiding.<br>
'''

EventData['RANGBAAZI'] = '''
Time limit - 2 Hours.<br><br>
1. Teams of maximum two members.<br>
2. Theme will be given on the spot.<br>
3. A4 sheets, poster colours and relevant materials will be provided on the
spot.<br>
4. No other material is allowed.<br>
5. Judging criteria: Creativity, relevance to the theme, uniqueness.<br>
6. The decision of judges will be final and abiding.<br>
'''

EventData['CLAY MODELLING'] = '''
Time limit: 3 hours<br>
1. Teams of maximum four members.<br>
2. All materials to be provided on spot.<br>
3. The theme will be given on spot.<br>
4. Judging Criteria: Creativity, Incorporation of the theme, Moulding skills,
Finishing, Uniqueness.<br>
5. The decision of the judges will be final & abiding<br>
'''

EventData['SOAP CARVING'] = '''
Time limit: 3 hours<br><br>
1. Teams of maximum two members.<br>
2. Theme will be given on the spot.<br>
3. Cutters, Soap, Fevicol, etc. will be provided.<br>
4. No additional materials are allowed.<br>
5. Judging Criteria: Creativity, Carving skills, Complexity of design,
Representation of the theme.<br>
6. The decision of the judges will be final & abiding.<br>
'''
EventData['FX MAKEUP'] = '''
Time limit - 3 hours.<br><br>
1. Team of maximum 3 members.<br>
2. A4 sheet, poster colors, cardboards, tissue paper, adhesive, brushes and
relevant materials will be provided.<br>
3. Teams can also bring other material of their own.<br>
4. Judging Criteria: Creativity, uniqueness, relevance to the theme.<br>
5. The decisions of the judges will be final and abiding<br>
'''
EventData['INK IT'] = '''
Time limit -2 hours.<br><br>
1. Team of maximum 2 members.<br>
2. A4 sheets, sketch pens, paints, brushes, etc will be provided.<br>
3. No additional materials are allowed.<br>
4. The decision of organisers will be final and abiding<br>
'''


EventData['SCRIPTURESQUE'] = '''
1. There'll be four sub-events under this—English Poetry Writing, English
Prose Writing, Hindi Poetry Writing, and Hindi Prose Writing.<br>
2. Topics will be given on the spot and 1 hour writing time is given.<br>
3. Judging criteria include creativity, style, and relevance to the topic.<br>
4. All the sub-events will be judged separately.<br>
5. Any plagiarism will result in disqualification.<br>
6. The decision of the judges is final.<br>
'''

EventData['BATTLEFRONT'] = '''
Preliminary Round<br><br>
Style: Turncoat<br><br>
1. It is an extempore event, so the topics will be provided on the spot and
each participant shall be given TWO minutes to prepare.<br>
2. The participants shall have to argue both sides of the topic themselves, that
is, they would be speaking both FOR and AGAINST the motion.<br>
3. The participants shall first speak FOR the motion of the house for TWO
MINUTES, and then SWITCH their stance to AGAINST the motion and speak for
another TWO MINUTES.<br>
4. The remaining time from one segment can't carry over to the other.<br>
5. The decision of the judges is final and profanity will be penalized with
disqualification.<br><br>
Final Round<br><br>
Style: British Parliamentary<br><br>
1. Following the prelims, all debates will be held in British Parliamentary (BP)
Format.<br>
2. The rules will be explained to the finalists at the venue.<br>
3. The speakers will be judged on manner, matter, and method<br>
'''

EventData['SHIPWRECK COVE'] = '''
Preliminary Round<br><br>
1. A hypothetical scenario presented depicts a ship full of famous personalities
that is wrecked and sinking. The judges (captains) have limited life jackets
remaining for the passengers.<br>
2. A personality is allotted to each contestant ONE minute before speaking, for
preparation.<br>
3. Participants must convince the captains as to why they deserve to be saved
(while sticking to their character). The speaking time is TWO minutes.<br>
4. Judging criteria include wit, delivery, and character portrayal.<br>
5. Witty innuendoes will earn you bonus points.<br><br>
Final Round<br><br>
1. All the rules of the preliminary round apply to the final round.<br>
2. An additional reply session will take place, where each contestant must<br>
convince the judges why the other passengers deserve to drown.<br>
'''

EventData['THE LEGEND OF SIR SPEAK-A-LOT'] = '''
1. The participants shall be required to compose an original poem or a speech
in ENGLISH, on a given topic, and deliver the same, with a maximum speaking
time of FIVE minutes.<br>
2. Participants will be judged on their content and delivery.<br>
3. Any plagiarism will result in disqualification.<br>
4. The decision of the judges is final.<br>
'''
EventData['A JESTERS COURT'] = '''
1. The stage is all yours for FIVE minutes!<br>
2. Both English and Hindi are allowed. No other language is allowed.<br>
3. Being bilingual is allowed.<br>
4. Use of obscenity/profanity (at the discretion of the judges) is not allowed
and there should be no direct implications.<br>
5. Judges to decide the winners for the comedy competition.<br>
6. Discretion of judges to be final and binding.<br>
'''


EventData['VAAD VIVAAD'] = '''
Preliminary Round<br><br>
1. It is an extempore event, so the topics will be provided on the spot, and
each participant shall be given TWO minutes to prepare.<br>
2. The participants can choose their stance and speak for a maximum of
THREE minutes.<br>
3. Judging criteria include content, organization and delivery.<br>
4. The decision of the judges is final and profanity will be penalized with
disqualification. The judges have final authority on determining the extent of
profanity.<br><br>
Final Round<br><br>
1. The rules will be explained to the finalists at the venue<br>
'''


EventData['ALFAAZ'] = '''
1. Topics are presented to the contestants ahead of time.<br>
2. The participants shall be required to compose an original poem or a speech
in HINDI, on a given topic, and deliver the same, with a maximum speaking
time of FIVE minutes.<br>
3. Participants will be judged on their content and delivery. Any plagiarism will
result in disqualification<br>
'''

EventData['ASHUBHASHAN'] = '''
Preliminary Round<br><br>
1. A personality is allotted to each contestant ONE minute before speaking, for
preparation.<br>
2. Participants must deliver a witty impromptu speech in Hindi, while sticking
to their character. The speaking time is TWO minutes.<br>
3. Judging criteria include wit, delivery, and character portrayal.<br>
4. Witty innuendoes will earn you bonus points.<br><br>
Final Round<br><br>
1. The rules will be explained to the finalists at the venue.<br>
'''

EventData["WHAT'S THE WORD?"] = '''
1. Contestants compete in teams of 2.<br>
2. A questionnaire containing various word puzzles and riddles is presented.<br>
3. Teams have 1 hour to solve all the questions.<br>
'''

EventData['SHORT FILM MAKING'] = '''
1. Each team should consist of max of 5 members.<br>
2. The film should be between 5 to 8 minutes including credits.<br>
3. The team should be present in the fest for the video to be taken into
consideration.<br>
4. Each of the team is required to shoot an aftermovie of Kashiyatra consisting
of the various glimpses of the fest.<br>
5. The Video must be shot in a resolution of 480p or greater. It can be shot on
any device, a DSLR or a phone or a Point-and-Shoot camera. The teams will
not be provided with any equipment or computers for editing or any other
purposes. <br>
6. The entire video must be shot during KY18.<br>
7. No special advantages will be given to any of the team. Like-entering into
the restricted areas.<br>
8. Completed movies (accompanied by the title of the video, name of the
college and details of team members) must be submitted in .mpeg or .avi or
.mp4 formats only in one of the following ways:<br>
• Upload the video to Google Drive and share access with events.kashiyatra@gmail.com. KY
ID of the team members must be separately mailed to above mail ID with subject to be
“SHORT FILM MAKING: Team name”.<br>
• Email to events.kashiyatra@gmail.com with subject of the email to be “SHORT FILM
MAKING: Team name”. Video and KY ID of the team members must be mentioned in the
content of the mail.<br>
• Upload the video on www.youtube.com and emailing the link to
events.kashiyatra@gmail.com with subject of the email to be “SHORT FILM MAKING:
Team name. Link and KY ID of the team members must be mentioned in the mail.
9. All the videos will be uploaded on the official youtube channel of
Kashiyatra.<br>
10. Judging criteria: The videos will be judged on the basis of no. of likes on
the video uploaded on the official youtube channel of Kashiyatra.<br>
11. Any plagiarism will result in disqualification.<br>
12. Deadline for submission is 1st February, 2018( BY 23:59 HRS).<br>
'''

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
                 ['INK IT',1, 2], ['SHORT FILM MAKING', 1, 5], ['FX MAKEUP', 1, 3]],
]
for i in CategoryList:
    print (i[0], '\n')
    parentevent = ParentEvent.objects.get(categoryName=i[0])
    for j in i[1:]:
        print(j)
        try:
            event = Event.objects.get(eventName=j[0], parentEvent=parentevent)
            event.eventDetails = EventData[j[0]]
            event.save()
        except Exception as e:
            print(e)
            print('exception for ', j[0])
            print('\n\n')
    print ('done!')