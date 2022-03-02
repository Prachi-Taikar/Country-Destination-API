from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.


Type_CHOICES = (
    ('city', 'CITY'),
    ('state', 'STATE'),
)

Type_CHOICES_city=(
    ('city', 'CITY'),
    ('locality', 'LOCALITY'),
)



#  ------- Country ----------
class Country(models.Model):
    countryName = models.CharField(max_length= 255)
    countryPhoto = models.ImageField(null = True, blank = True)


    def __str__(self):
        return self.countryName


# -----------country type Location ----------

class TypeLocation(models.Model):
    countryName = models.ForeignKey(Country, on_delete=models.CASCADE)
    type = models.CharField(max_length=200, choices=Type_CHOICES, default='', null=True, blank=True)
    location = models.CharField(max_length=200, null=False, blank=False)
    tlPhoto = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.location

# ------------cityLocality---------

class CityLocality(models.Model):
    countryName = models.ForeignKey(Country, on_delete=models.CASCADE)
    location = models.ForeignKey(TypeLocation, on_delete=models.CASCADE)
    type= models.CharField(max_length=200, choices=Type_CHOICES_city, default='', null=True, blank=True)
    cityLocation = models.CharField(max_length=200, null=False, blank=False)
    clPhoto= models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.cityLocation


# --------------------LocationLocation----------

class LocationLoc(models.Model):
    countryName = models.ForeignKey(Country, on_delete=models.CASCADE)
    location = models.ForeignKey(TypeLocation, on_delete=models.CASCADE)
    cityLocation= models.ForeignKey(CityLocality, on_delete=models.CASCADE)
    subLocation = models.CharField(max_length=200, null=True, blank=True)
    llPhoto = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.subLocation






