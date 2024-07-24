from django.db import models
from salle_reunion.models import Personnel, Financement

class Marque(models.Model):
    nom_marque = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'marque'


class Modele(models.Model):
    id_marque = models.ForeignKey(Marque, models.DO_NOTHING, db_column='id_marque', blank=True, null=True)
    nom_modele = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'modele'

class Vehicule(models.Model):
    num_vehicule = models.CharField(primary_key=True, max_length=12)
    id_modele = models.ForeignKey(Modele, models.DO_NOTHING, db_column='id_modele', blank=True, null=True)
    id_financement = models.ForeignKey(Financement, models.DO_NOTHING, db_column='id_financement', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicule'


class VehiculeMission(models.Model):
    id_mission = models.AutoField(primary_key=True)
    debut = models.DateField()
    fin = models.DateField()
    id_chauffeur = models.ForeignKey(Personnel, models.DO_NOTHING, db_column='id_chauffeur', blank=True, null=True)
    id_chef_mission = models.ForeignKey(Personnel, models.DO_NOTHING, db_column='id_chef_mission', related_name='vehiculemission_id_chef_mission_set', blank=True, null=True)
    num_vehicule = models.ForeignKey(Vehicule, models.DO_NOTHING, db_column='num_vehicule', blank=True, null=True)
    lieu = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicule_mission'

class DetailVehiculeMission(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()
    nom_chauffeur = models.CharField(max_length=255)
    prenom_chauffeur = models.CharField(max_length=255)
    code_chauffeur = models.CharField(max_length=50)
    nom_chef_mission = models.CharField(max_length=255)
    prenom_chef_mission = models.CharField(max_length=255)
    code_chef_mission = models.CharField(max_length=50)
    num_vehicule = models.CharField(max_length=50)
    nom_modele = models.CharField(max_length=255)
    nom_marque = models.CharField(max_length=255)
    nom_bailleur = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'v_detail_vehicule_mission'

    def __str__(self):
        return self.objet

# Create your models here.
