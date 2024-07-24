from django.contrib.auth.models import User
from .models import Personnel
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

"""class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return {
            "username": user.username,
            "email": user.email
        }"""
    
class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ['username', 'email', 'phone', 'gender', 'first_name', 'last_name', 'is_active', 'id_financement', 'id_fonction', 'id_lieu_affectation', 'code', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Ajouter des champs personnalisés au JWT
        token['code'] = user.code

        return token