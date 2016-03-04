from rest_framework import serializers
from models import State,County,City,Zip

class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		field = ('id','name')
		
class CountySerializer(serializers.ModelSerializer):
	class Meta:
		model = County
		field = ('id','name')
		
class StateSerializer(serializers.ModelSerializer):
	class Meta:
		model = State
		field = ('id','name','state_abbr')

#many=True,read_only = True		
class ZipSerializer(serializers.ModelSerializer):
	city   = CitySerializer()
	county = CountySerializer()
	state  = StateSerializer()
	
	class Meta:
		model = Zip
		field = ('id','zipcode','city','county','state')
