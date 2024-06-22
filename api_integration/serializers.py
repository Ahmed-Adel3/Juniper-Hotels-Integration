from rest_framework import serializers
from .models import HotelDoLog


class HotelDoLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelDoLog
        fields = ['id', 'method', 'request',
                  'response', 'error', 'created_date']
