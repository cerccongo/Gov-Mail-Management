from django.db import models
from django.contrib.auth.models import User

class PieceJointe(models.Model):
    fichier = models.FileField(upload_to="pieces_jointes/")
    nom = models.CharField(max_length=255)

class CourrierEntrant(models.Model):
    date_reception = models.DateField()
    numero_enregistrement = models.CharField(max_length=50, unique=True)
    objet = models.CharField(max_length=255)
    expediteur = models.CharField(max_length=255)
    destinataire_interne = models.CharField(max_length=100)
    statut = models.CharField(max_length=30)
    pieces_jointes = models.ManyToManyField(PieceJointe, blank=True)
    observations = models.TextField(blank=True)
    cree_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class CourrierSortant(models.Model):
    date_transmission = models.DateField()
    objet = models.CharField(max_length=255)
    numero_reference = models.CharField(max_length=50, unique=True)
    destinataire = models.CharField(max_length=255)
    statut = models.CharField(max_length=30)
    recu_par = models.CharField(max_length=255, blank=True)
    pieces_jointes = models.ManyToManyField(PieceJointe, blank=True)
    lien_courrier_entrant = models.ForeignKey(
        CourrierEntrant, null=True, blank=True, on_delete=models.SET_NULL
    )
    cree_par = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
