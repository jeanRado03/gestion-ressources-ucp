from rest_framework import serializers
from personnel.models import StatutAbsencePersonnel, DetailStatutAbsencePersonnel

class StatutAbsencePersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatutAbsencePersonnel
        fields = '__all__'

class DetailStatutAbsencePersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailStatutAbsencePersonnel
        fields = '__all__'