from django.urls import path, include
from .views import CountryViewSet, TypeLocationViewSet, CityLocaViewSet, LocLocaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('country', CountryViewSet, basename = 'country')
router.register('typeLoc', TypeLocationViewSet, basename = 'typeLocation')
router.register('cityLoc', CityLocaViewSet, basename = 'cityLocality')
router.register('locLoca', LocLocaViewSet, basename = 'locLocality')

urlpatterns = [
    path('destinationCountry/', include(router.urls)),
    
]