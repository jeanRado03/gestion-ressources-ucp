from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from datetime import datetime
from vehicule.models import VehiculeMission, DetailVehiculeMission
from .serializers import VehiculeMissionSerializer, DetailVehiculeMissionSerializer

class AddVehiculeMissionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = VehiculeMissionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def updateVehiculeMission(request, pk):
    try:
        vehicule_mission = VehiculeMission.objects.get(pk=pk)
        serializer = VehiculeMissionSerializer(vehicule_mission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except VehiculeMission.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def deleteVehiculeMission(request, pk):
    try:
        vehicule_mission = VehiculeMission.objects.get(pk=pk)
        vehicule_mission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Salle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class DetailReservationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            detail_vehicule = DetailVehiculeMission.objects.all()
            serializer = DetailVehiculeMissionSerializer(detail_vehicule, many=True)

            return Response({'status': 200, 'message': 'OK', 'data': serializer.data, 'error': None}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)