from django.shortcuts import render
from rest_framework import viewsets,generics
from serializers import ZipSerializer,StateSerializer
from models import Zip,City,County,State

class ZipList(generics.ListCreateAPIView):
	queryset = Zip.objects.all()
	serializer_class = ZipSerializer
	
class ZipDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Zip.objects.all()
	serializer_class = ZipSerializer	
	
class StateViewSet(viewsets.ModelViewSet):
	queryset = State.objects.all()
	serializer_class = StateSerializer
