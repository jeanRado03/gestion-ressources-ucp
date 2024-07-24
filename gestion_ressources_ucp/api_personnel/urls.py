from django.urls import path
from . import views
from .views import AddStatutAbsencePersonnelView, DetailStatutAbsencePersonnelView

urlpatterns = [
    path('personnels-absents/', DetailStatutAbsencePersonnelView.as_view()),
    path('personnels-absent/ajout/', AddStatutAbsencePersonnelView.as_view()),
    path('personnels-absent/modification/<int:pk>', views.updateStatutAbscencePersonnel),
    path('personnels-absent/suppression/<int:pk>', views.deleteStatutAbsencePersonnel),
]