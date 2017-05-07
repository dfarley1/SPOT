from rest_framework import serializers
from sensor.models import structures

class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = structures
        fields = ('name',)
