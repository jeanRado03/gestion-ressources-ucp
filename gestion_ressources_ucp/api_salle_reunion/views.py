from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from salle_reunion.models import Salle, Personnel, Financement, ReservationSalle, DetailReservationSalle
from .serializers import SalleSerializer, DemandeurSerializer, FinancementSerializer, ReservationSalleSerializer, DetailReservationSerializer
from django.shortcuts import get_object_or_404
from datetime import datetime
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token
import jwt
from django.conf import settings


class SallesListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            salles = Salle.objects.all()
            serializer = SalleSerializer(salles, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def addSalle(request):
    try:
        serializer = SalleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getSalleById(request, pk):
    try:
        salle = Salle.objects.get(pk=pk)
        serializer = SalleSerializer(salle)
        return Response(serializer.data)
    except Salle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def updateSalle(request, pk):
    try:
        salle = Salle.objects.get(pk=pk)
        serializer = SalleSerializer(salle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Salle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def deleteSalle(request, pk):
    try:
        salle = Salle.objects.get(pk=pk)
        salle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Salle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
## API Demandeur ##
"""@api_view(['GET'])
def getDemandeurs(request):
    try:
        demandeurs = Personnel.objects.all()
        serializer = DemandeurSerializer(demandeurs, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def addDemandeur(request):
    try:
        serializer = DemandeurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getDemandeurById(request, pk):
    try:
        demandeur = Personnel.objects.get(pk=pk)
        serializer = DemandeurSerializer(demandeur)
        return Response(serializer.data)
    except Personnel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateDemandeur(request, pk):
    try:
        demandeur = Personnel.objects.get(pk=pk)
        serializer = DemandeurSerializer(demandeur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Personnel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteDemandeur(request, pk):
    try:
        demandeur = Personnel.objects.get(pk=pk)
        demandeur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Personnel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)"""

## API Financement ##
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getFinancements(request):
    try:
        financements = Financement.objects.all()
        serializer = FinancementSerializer(financements, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def addFinancement(request):
    try:
        serializer = FinancementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getFinancementById(request, pk):
    try:
        financement = Financement.objects.get(pk=pk)
        serializer = FinancementSerializer(financement)
        return Response(serializer.data)
    except Financement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def updateFinancement(request, pk):
    try:
        financement = Financement.objects.get(pk=pk)
        serializer = FinancementSerializer(financement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Financement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def deleteFinancement(request, pk):
    try:
        financement = Financement.objects.get(pk=pk)
        financement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Financement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

## API Reservation ##
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getReservations(request):
    try:
        reservations = ReservationSalle.objects.all()
        serializer = ReservationSalleSerializer(reservations, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddReservationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = ReservationSalleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getReservationById(request, pk):
    try:
        reservation = ReservationSalle.objects.get(pk=pk)
        serializer = ReservationSalleSerializer(reservation)
        return Response(serializer.data)
    except ReservationSalle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
def check_authorization(reservation, user_id):
    if user_id != reservation.id_demandeur.id:
        print(user_id)
        print(reservation.id_demandeur.id)
        raise Exception("Vous n'avez pas l'autorisation de modifier ou supprimer cette réservation.")
    
def verifier_reunion_en_cours(reservation):
    now = datetime.utcnow()
    if reservation.debut <= now <= reservation.fin:
        raise Exception("La réunion est en cours, modification ou suppression impossible")

@api_view(['PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def updateReservation(request, pk):
    try:
        reservation = ReservationSalle.objects.get(pk=pk)
        user_id = request.data.get('user_id')
        check_authorization(reservation, user_id)
        verifier_reunion_en_cours(reservation)

        serializer = ReservationSalleSerializer(reservation, data=request.data.get('data', {}))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ReservationSalle.DoesNotExist:
        return Response({'status': 404, 'message': 'NOT FOUND', 'data': None, 'error': 'Not Found Exception'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'status': 500, 'message': 'INTERNAL SERVER ERROR', 'data': None, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def deleteReservation(request, pk):
    try:
        reservation = ReservationSalle.objects.get(pk=pk)
        token = request.auth.decode('utf-8')

        print(token)
        
        decoded_token = jwt.decode(token, options={"verify_signature": False})  # Décoder le token sans vérification
        
        user_id = decoded_token.get('user_id')  # Récupérer l'user_id du token
        
        if not user_id:
            return Response({'status': 400, 'message': 'BAD REQUEST', 'data': None, 'error': 'User ID manquant dans le token'}, status=status.HTTP_400_BAD_REQUEST)
        
        print('user_id' + str(user_id))
        check_authorization(reservation, user_id)
        verifier_reunion_en_cours(reservation)

        reservation.delete()
        return Response({'status': 204, 'message': 'NO CONTENT', 'data': None, 'error': None},status=status.HTTP_204_NO_CONTENT)
    except Financement.DoesNotExist:
        return Response({'status': 404, 'message': 'NOT FOUND', 'data': None, 'error': 'Not Found Exception'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'status': 500, 'message': 'INTERNAL SERVER ERROR', 'data': None, 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
## Detail View Resrvation ##

class DetailReservationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            current_date = datetime.now().date()
            detail_reservations = DetailReservationSalle.objects.filter(fin__date__gte=current_date)
            serializer = DetailReservationSerializer(detail_reservations, many=True)

            return Response({'status': 200, 'message': 'OK', 'error': None, 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['GET'])
def dateHeureActuelle(request):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return Response({'status': 200, 'message': 'OK', 'date': current_datetime}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def getDetailReservationByIdSalle(request, pk=None):
    try:
        queryset = DetailReservationSalle.objects.filter(id_salle=pk)
        if queryset.exists():
            serializer = DetailReservationSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except DetailReservationSalle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)