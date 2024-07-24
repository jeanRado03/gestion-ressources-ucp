from django.db import models
from salle_reunion.models import Personnel

class StatutAbsence(models.Model):
    statut = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'statut_absence'


class StatutAbsencePersonnel(models.Model):
    debut = models.DateField()
    fin = models.DateField()
    id_personnel = models.ForeignKey(Personnel, models.DO_NOTHING, db_column='id_personnel', blank=True, null=True)
    id_statut_absence = models.ForeignKey(StatutAbsence, models.DO_NOTHING, db_column='id_statut_absence', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statut_absence_personnel'

class DetailStatutAbsencePersonnel(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()
    id_personnel = models.IntegerField()
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    code = models.CharField(max_length=50)
    nom_bailleur = models.CharField(max_length=255)
    id_statut_absence = models.IntegerField()
    statut = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'v_detail_statut_absence_personnel'

    def __str__(self):
        return self.objet

# Create your models here.
