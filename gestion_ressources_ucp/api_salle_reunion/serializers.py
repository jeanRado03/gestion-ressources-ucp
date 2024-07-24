from rest_framework import serializers
from salle_reunion.models import Salle, Financement, Personnel, ReservationSalle, DetailReservationSalle

class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = '__all__'

class DemandeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = '__all__'

class FinancementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Financement
        fields = '__all__'

class ReservationSalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationSalle
        fields = '__all__'

class DetailReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailReservationSalle
        fields = '__all__'