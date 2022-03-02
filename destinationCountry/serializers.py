from rest_framework import serializers
from .models import Country
from .models import TypeLocation
from .models import CityLocality
from .models import LocationLoc

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class TypeLocSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeLocation
        fields = '__all__'

class CityLocaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityLocality
        fields = '__all__'

class LocLocaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationLoc
        fields = '__all__'