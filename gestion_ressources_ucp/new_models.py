# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    gender = models.CharField(max_length=1)
    phone = models.CharField(max_length=30, blank=True, null=True)
    id_financement = models.ForeignKey('Financement', models.DO_NOTHING, db_column='id_financement', blank=True, null=True)
    id_fonction = models.ForeignKey('Fonction', models.DO_NOTHING, db_column='id_fonction', blank=True, null=True)
    id_lieu_affectation = models.ForeignKey('Centre', models.DO_NOTHING, db_column='id_lieu_affectation', blank=True, null=True)
    code = models.CharField(unique=True, max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Centre(models.Model):
    lieu = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'centre'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Financement(models.Model):
    nom_bailleur = models.CharField(unique=True, max_length=125, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financement'


class Fonction(models.Model):
    nom_fonction = models.CharField(max_length=70, blank=True, null=True)
    id_service = models.ForeignKey('Services', models.DO_NOTHING, db_column='id_service', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonction'


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


class ReservationSalle(models.Model):
    debut = models.DateTimeField()
    fin = models.DateTimeField()
    id_salle = models.ForeignKey('Salle', models.DO_NOTHING, db_column='id_salle', blank=True, null=True)
    id_financement = models.ForeignKey(Financement, models.DO_NOTHING, db_column='id_financement', blank=True, null=True)
    id_demandeur = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_demandeur', blank=True, null=True)
    objet = models.TextField(blank=True, null=True)
    participant = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservation_salle'


class Salle(models.Model):
    nom_salle = models.CharField(unique=True, max_length=125, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salle'


class Services(models.Model):
    nom_service = models.CharField(unique=True, max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'


class StatutAbsence(models.Model):
    statut = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'statut_absence'


class StatutAbsencePersonnel(models.Model):
    debut = models.DateField()
    fin = models.DateField()
    id_personnel = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_personnel', blank=True, null=True)
    id_statut_absence = models.ForeignKey(StatutAbsence, models.DO_NOTHING, db_column='id_statut_absence', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statut_absence_personnel'


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
    id_chauffeur = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_chauffeur', blank=True, null=True)
    id_chef_mission = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_chef_mission', related_name='vehiculemission_id_chef_mission_set', blank=True, null=True)
    num_vehicule = models.ForeignKey(Vehicule, models.DO_NOTHING, db_column='num_vehicule', blank=True, null=True)
    lieu = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehicule_mission'
