from django.urls import path
from . import views
from .views import SallesListView, DetailReservationsView, AddReservationView

urlpatterns = [
    #path('salles/', views.getSalles),
    path('salles/', SallesListView.as_view()),
    path('salle/<int:pk>/', views.getSalleById),
    #path('demandeurs/', views.getDemandeurs),
    #path('demandeur/<int:pk>/', views.getDemandeurById),
    path('financements/', views.getFinancements),
    path('financement/<int:pk>/', views.getFinancementById),
    path('reservations/', views.getReservations),
    #path('reservation/ajout/', views.addReservation),
    path('reservation/ajout/', AddReservationView.as_view()),
    path('reservation/<int:pk>/', views.getReservationById),
    path('reservation/modification/<int:pk>/', views.updateReservation),
    path('reservation/suppression/<int:pk>/', views.deleteReservation),
    path('detail-reservations/', DetailReservationsView.as_view()),
    path('detail-reservation/<int:pk>/', views.getDetailReservationByIdSalle),
    path('date-heure-actuelle', views.dateHeureActuelle),
]