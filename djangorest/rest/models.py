from __future__ import unicode_literals

from django.db import models

class State(models.Model):
	name = models.CharField(max_length=90,unique=True, blank=True)
	state_abbr = models.CharField(max_length=24,blank=True,unique=True)
	
	def __unicode__(self):
		return self.name
		
class County(models.Model):
	name = models.CharField(max_length=96,unique=True,blank=True)
	
	def __unicode__(self):
		return self.name

class City(models.Model):
	name = models.CharField(max_length=96,unique=True, blank = True)
	
	def __unicode__(self):
		return self.name

class Zip(models.Model):
	zipcode = models.CharField(max_length=12,unique=True)
	state   = models.ForeignKey(State)
	county  = models.ForeignKey(County)
	city    = models.ForeignKey(City)
