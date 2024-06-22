from django.db import models
from django.utils import timezone

class Zone(models.Model):
    jpd_code = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.jpd_code)


class City(models.Model):
    jpd_code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.jpd_code)


class HotelCategory(models.Model):
    type = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.code)
    

class Hotel(models.Model):
    jp_code = models.CharField(max_length=20)
    has_synonyms = models.BooleanField()
    name = models.CharField(max_length=255)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    hotel_category = models.ForeignKey(HotelCategory, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return str(self.jp_code)

    class Meta:
        ordering = ['id']


class HotelDoLog(models.Model):
    id = models.AutoField(primary_key=True)
    method = models.CharField(max_length=20)
    request = models.TextField()
    response = models.TextField()
    error = models.BooleanField()
    created_date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self) -> str:
        return str(self.method)

    class Meta:
        ordering = ['id']