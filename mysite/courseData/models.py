from django.db import models
from django.core.validators import int_list_validator

#class University(models.Model):

#class Major(models.Model):
    
class Course(models.Model):
	SUBJECT_CHOICES=(
		('ACCT', 'ACCT - Accounting'),
		('ACTS', 'ACTS - Actuarial Science'),
		('AHST', 'AHST - Art History'),
		('AMS', 'AMS - American Studies'),
		('AP', 'AP - Art and Performance'),
		('ARAB', 'ARAB - Arabic'),
		('ARHM', 'ARHM - Arts and Humanities'),
		('ARTS', 'ARTS - Art'),
		('ATCM', 'ATCM - Arts Tech and Comm'),
		('ATEC', 'ATEC - Arts and Tech'),
		('ATEM', 'ATEM - Arts Tech and Emmerging Comm'),
		('AUD', 'AUD - Audiology'),
		('BA', 'BA - Business Admin'),
		('BCOM', 'BCOM - Business Comm'),
		('BIOL', 'BIOL - Biology'),
		('BIS', 'BIS - Interdisciplinary Studies'),
		('BLAW', 'BLAW - Business Law'),
		('BMEN', 'BMEN - Biomedical Engineering'),
		('BPS', 'BPS - Business Policy and Strategy'),
		('CE', 'CE - Computer Engineering'),
		('CGS', 'CGS - Cognitive Science'),
		('CHEM', 'CHEM - Chemistry'),
		('CHIN', 'CHIN - Chinese'),
		('CLDP', 'CLDP - Child Learning and Development'),
		('COMM', 'COMM - Communications'),
		('CRIM', 'CRIM - Criminology'),
		('CRWT', 'CRWT - Creative Writing'),
		('CS', 'CS - Computer Science'),
		('DANC', 'DANC - Dance'),
		('ECON', 'ECON - Economics'),
		('ECS', 'ECS - Engineering and Computer Science'),
		('ECSC', 'ECSC - Engineering and Computer Science COOP'),
		('ED', 'ED - Education'),
		('EE', 'EE - Electrical Engineering'),
		('EMAC', 'EMAC - Emmerging Media and Communications'),
		('ENGR', 'ENGR - Engineering'),
		('ENGY', 'ENGY - Energy Management'),
		('ENTP', 'ENTP - Innovation and Entrepeneurship'),
		('ENVR', 'ENVR - Environmental Science'),
		('EPPS', 'EPPS - Economic, Political, and Policy Sciences'),
		('FILM', 'FILM - Film Studies'),
		('FIN', 'FIN - Finance'),
		('FREN', 'FREN - French'),
		('GEOG', 'GEOG - Geography'),
		('GEOS', 'GEOS - Geosciences'),
		('GERM', 'GERM - German'),
		('GISC', 'GISC - Geospatial Information Sciences'),
		('GOVT', 'GOVT - Government'),
		('GST', 'GST - Gender Studies'),
		('HIST', 'HIST - History'),
		('HLTH', ' HLTH - Health Care Studies'),
		('HMGT', 'HMGT - Healthcare Management'),
		('HONS', 'HONS - Honors College'),
		('HUMA', 'HUMA - Humanities'),
		('IMS', 'IMS - International Management Studies'),
		('IPEC', 'IPEC - International Political Economy'),
		('ISAE', 'ISAE - Interdisciplinary Studies - Arts Tech and Emmerging Comm'),
		('ISAH', 'ISAH - Interdisciplinary Studies - Arts and Humanities'),
		('ISEC', 'ISEC - Interdisciplinary Studies - Electrical Engineering and Computer Science'),
		('ISIS', 'ISIS - Interdisciplinary Studies'),
		('ISNS', 'ISNS - Interdisciplinary Studies - Natural Science and Mathematics'),
		('ISSS', 'ISSS - Interdisciplinary Studies - Social Science'),
		('ITSS', 'ITSS - Information Technologies and Systems'),
		('JAPN', 'JAPN - Japanese'),
		('LANG', 'LANG - Language'),
		('LIT', 'LIT - Literary Studies'),
		('MATH', 'MATH - Mathematical Science'),
		('MECH', 'MECH - Mechanical Engineering'),
		('MECO', 'MECO - Managerial Economics'),
		('MKT', 'MKT - Marketing Management'),
		('MUSI', 'MUSI - Music'),
		('NANO', 'NANO - Nanoscience'),
		('NATS', 'NATS - Natural Sciences'),
		('NSC', 'NSC - Neuroscience'),
		('OBHR', 'OBHR - Organizational Behaviour/Human Resources'),
		('OPRE', 'OPRE - Operations Research'),
		('PA', 'PA - Public Affairs Management'),
		('PHIL', 'PHIL - Philosophy'),
		('PHIN', 'PHIN - Physical Instruction'),
		('PHYS', 'PHYS - Physics'),
		('PPOL', 'PPOL - Public Policy'),
		('PSCI', 'PSCI - Political Science'),
		('PSY', 'PSY - Psychology'),
		('REAL', 'REAL - Real Estate'),
		('RHET', 'RHET - Rhetoric'),
		('RMIS', 'RMIS - Risk Management and Insurance'),
		('SE', 'SE - Software Engineering'),
		('SOC', 'SOC - Sociology'),
		('SOCS', 'SOCS - Social Sciences'),
		('SPAN', 'SPAN - Spanish'),
		('SPAW', 'SPAW - Speech - Language Pathology and Audiology'),
		('STAT', 'STAT - Statistics'),
		('TE', 'TE - Telecommunications Engineering'),
		('THEA', 'THEA - Theatre'),
		('UNIV', 'UNIV - University Course'),
		('DMTH', 'DMTH - Developmental Math'),
		('DRDG', 'DRDG - Developmental Reading'),
		('DWTG', 'DWTG - Developmental Writing'),
		)
	subj = models.CharField("Subject", max_length=4, choices=SUBJECT_CHOICES, default="ACCT")
	x = int_list_validator(sep='', message='Invalid input', code='invalid', allow_negative=False)
	class_num = models.CharField("Class number", max_length=4, default="0000", validators=[x])
	prereq = models.ForeignKey('self', on_delete=models.CASCADE, related_name='Pre-requisite+', null=True, blank=True)
	coreq = models.OneToOneField('self',  on_delete=models.CASCADE, related_name='Co-requisite+', null=True, blank=True)
	#prereq = models.ManyToManyField("self", "Pre-requisite Courses", blank=True)
	def __str__(self):
		return "%s %s" % (self.subj, self.class_num)
    
'''class Prereq(models.Model):
	dept = models.CharField("Department", max_length=4, default="ACCT")
	x = int_list_validator(sep='', message='Invalid input', code='invalid', allow_negative=False)
	class_num = models.CharField("Class number", max_length=4, default="0000",  validators=[x])
	postreq = models.ForeignKey('Course', on_delete=models.CASCADE, blank=True, default=None)
'''

'''class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)from django.db import models
'''
# Create your models here.
