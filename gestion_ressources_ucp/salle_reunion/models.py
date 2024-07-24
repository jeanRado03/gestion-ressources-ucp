from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser, PermissionsMixin

class Salle(models.Model):
    nom_salle = models.CharField(unique=True, max_length=125, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salle'

class Centre(models.Model):
    lieu = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'centre'

class Services(models.Model):
    nom_service = models.CharField(unique=True, max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'

class Fonction(models.Model):
    nom_fonction = models.CharField(max_length=70, blank=True, null=True)
    id_service = models.ForeignKey(Services, models.DO_NOTHING, db_column='id_service', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonction'


class Financement(models.Model):
    nom_bailleur = models.CharField(unique=True, max_length=125, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financement'

class PersonnelManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'email est requis')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Personnel(AbstractUser):
    gender = models.CharField(max_length=1)
    phone = models.CharField(max_length=30, blank=True, null=True)
    id_financement = models.ForeignKey('Financement', models.DO_NOTHING, db_column='id_financement', blank=True, null=True)
    id_fonction = models.ForeignKey('Fonction', models.DO_NOTHING, db_column='id_fonction', blank=True, null=True)
    id_lieu_affectation = models.ForeignKey('Centre', models.DO_NOTHING, db_column='id_lieu_affectation', blank=True, null=True)
    code = models.CharField(unique=True, max_length=45, blank=True, null=True)

    objects = PersonnelManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        managed = False
        db_table = 'auth_user'


class ReservationSalle(models.Model):
    debut = models.DateTimeField()
    fin = models.DateTimeField()
    id_salle = models.ForeignKey(Salle, models.DO_NOTHING, db_column='id_salle', blank=True, null=True)
    id_financement = models.ForeignKey(Financement, models.DO_NOTHING, db_column='id_financement', blank=True, null=True)
    id_demandeur = models.ForeignKey(Personnel, models.DO_NOTHING, db_column='id_demandeur', blank=True, null=True)
    objet = models.TextField(blank=True, null=True)
    participant = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservation_salle'
        
class DetailReservationSalle(models.Model):
    id_reservation = models.AutoField(primary_key=True)
    debut = models.DateTimeField()
    fin = models.DateTimeField()
    id_salle = models.IntegerField()
    salle = models.CharField(max_length=100)
    financement = models.CharField(max_length=100)
    objet = models.TextField()
    participant = models.IntegerField()
    demandeur = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'v_reservation_salle'

    def __str__(self):
        return self.objet
# Create your models here.
