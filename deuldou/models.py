
from django.contrib.auth.models import User
from django.core.exceptions import (ObjectDoesNotExist, PermissionDenied,
                                    ValidationError)
from django.db import models
from django.utils import timezone

# Create your models here.


class Tag(models.Model):
    """
    Une étiquette permet de marquer l'invitation à l'aide d'un mot-clé
    afin de regrouper les invitations par mot-clé (pour l'affichage)
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='etiquettes')
    nom = models.CharField(max_length=100)
    is_checked = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class Deuldou(models.Model):
    # attributs
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="deuldous_crees")
    created_at = models.DateTimeField(default=timezone.now)
    nom = models.CharField(max_length=100, null=False)
    jour = models.DateField(null=False)
    heure_debut = models.TimeField(default='00:00')
    heure_fin = models.TimeField(default='00:00', blank=True)
    lieu = models.TextField(null=False, max_length=100)
    # config :
    # nombre min = minimum de participants à participer pour valider le rdv
    nbre_min = models.IntegerField(default=0)
    #createur_participe = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
    
    @classmethod
    def get_for_user(cls,rdv_id,user):
        rdv = Deuldou.objects.get(pk=rdv_id)
        if rdv.created_by != user:
            raise PermissionDenied()
        return rdv


class Participant(models.Model):
    """ ------------ Choix -------- """
    PRESENT = "PR"
    ABSENT = "AB"
    RETARD = "RE"
    INCERTAIN = "IN"
    PISCINE = "PI"
    VITE_FAIT = "VI"
    NON_INSCRIT = "NI"
    STATUTS_CHOICES = [
        (PRESENT, "Présent"),
        (ABSENT, "Absent"),
        (RETARD, "En retard"),
        (INCERTAIN, "Incertain"),
        (PISCINE,"Peux pas j'ai piscine"),
        (VITE_FAIT, "Je passe pour dire bonjour"),
        (NON_INSCRIT, "Non inscrit")
    ]
    """ ------------ Obligatoire-------- """
    rdv = models.ForeignKey(Deuldou, on_delete=models.CASCADE, related_name='participants')
    email = models.EmailField(max_length=100, blank=False)
    nom = models.CharField(max_length=150, blank=False)
    """ ------------ Facultatif-------- """
    statut = models.CharField(max_length=2,choices=STATUTS_CHOICES,default=NON_INSCRIT)#, "Non inscrit"))
    visible = models.BooleanField(default=True)
    commentaire = models.TextField(null=True, blank=True)
    #tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.nom
    
    """
    Contrainte unique sur les clés RDV et EMAIL    
    """
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["rdv", "email"], name='participation unique', violation_error_message="Ce participant existe déjà"),
        ]
    
    @classmethod
    def get_for_user(cls, participant_id:int, user:User):
        participant: Participant = cls.objects.get(pk=participant_id)
        if participant.email != user.email:
            raise PermissionDenied()
        return participant
    

""" ----------------  CONTACTS ----------------------- """


class Contact(models.Model):
    """
    Contraintes :
    - Un contact appartient à UN User et un user peut avoir des contacts et des listes de contacts
    - Un User ne peut pas avoir 2 contacts avec la même adresse email
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    email = models.EmailField(max_length=150, blank=False)
    nom = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.nom
    
    def clean(self) -> None:
        """
        Un User ne peut pas être Contact de lui même :
        """
        if self.user.email == self.email :
            raise ValidationError({"email": "Vous ne pouvez pas vous ajouter comme Contact"})
        
    @classmethod
    def get_for_user(cls, pk:int, user:User):
        contact: Contact = cls.objects.get(pk=pk)
        if contact.user != user:
            raise PermissionDenied()
        return contact
        
    """
    Contrainte unique sur les clés USER et EMAIL    
    """
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "email"], name='contact unique', violation_error_message="Ce contact existe déjà")
        ]


class ListeContacts(models.Model):
    """
    Un User peut enregistrer plusieurs listes
    Un contact peut appartenir à plusieurs listes (exemple, contact(seb) appartient à entrainement et matchs)
    contraintes:
    - unique pour : USER et NOM
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_listes_contacts')
    nom = models.CharField(max_length=100, blank=False, null=False)
    contacts = models.ManyToManyField(Contact)

    class Meta:
        ordering = ['nom']
        constraints = [
            models.UniqueConstraint(
                fields=["user", "nom"], name='liste unique', violation_error_message="Cette liste existe déjà")
        ]

    def __str__(self):
        return self.nom
    
    
""" ----------------  FIN DES CONTACTS ----------------------- """