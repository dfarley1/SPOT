from rest_framework import serializers
from sensor.models import *

class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = structures
        fields = ('name',)

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = spot_data 
        fields = ('uuid','active','section','number','description','gpslat','gpslon', 'rate','last_update','occ_status','occ_since','occ_license','occupant')
