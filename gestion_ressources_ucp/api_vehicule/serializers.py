from rest_framework import serializers
from vehicule.models import VehiculeMission, DetailVehiculeMission

class VehiculeMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculeMission
        fields = '__all__'

class DetailVehiculeMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailVehiculeMission
        fields = '__all__'