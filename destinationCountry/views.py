
from django.shortcuts import render, HttpResponse
from .models import Country, TypeLocation, CityLocality, LocationLoc
from rest_framework import viewsets
from .serializers import CountrySerializer, TypeLocSerializer, CityLocaSerializer, LocLocaSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class TypeLocationViewSet(viewsets.ModelViewSet):
    queryset = TypeLocation.objects.all()
    serializer_class = TypeLocSerializer

class CityLocaViewSet(viewsets.ModelViewSet):
    queryset = CityLocality.objects.all()
    serializer_class = CityLocaSerializer

class LocLocaViewSet(viewsets.ModelViewSet):
    queryset = LocationLoc.objects.all()
    serializer_class = LocLocaSerializer