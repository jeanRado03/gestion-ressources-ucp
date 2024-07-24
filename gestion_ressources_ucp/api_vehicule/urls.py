from django.urls import path
from . import views
from .views import AddVehiculeMissionView, DetailReservationsView

urlpatterns = [
    path('vehicules-en-missions/', DetailReservationsView.as_view()),
    path('vehicule-en-mission/ajout/', AddVehiculeMissionView.as_view()),
    path('vehicule-en-mission/modification/<int:pk>', views.updateVehiculeMission),
    path('vehicule-en-mission/suppression/<int:pk>', views.deleteVehiculeMission),
]