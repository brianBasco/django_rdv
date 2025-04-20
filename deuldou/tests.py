from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.test import TestCase

from .models import Deuldou, Invite, Participant, Tag, User
from .services import *


class DeuldouTestCase(TestCase):

    def setUp(self):
        seb = User.objects.create_user(
            username="seb", email="seb@gmail.com", password="mdp")
        marie = User.objects.create_user(
            username="marie", email="marie@gmail.com", password="mdp")
        ju = User.objects.create_user(
            username="ju", email="ju@gmail.com", password="mdp")
        sego = User.objects.create_user(
            username="sego", email="sego@gmail.com", password="mdp")
        sylvain = User.objects.create_user(
            username="sylvain", email="sylvain@gmail.com", password="mdp")
        amine = User.objects.create_user(
            username="Amine", email="amine@gmail.com", password="mdp")
        fred = User.objects.create_user(
            username="Fred", email="fred@gmail.com", password="mdp")

        match_etiquette = Tag()
        match_etiquette.nom = "match"
        match_etiquette.user = seb

        entrainement_etiquette = Tag()
        entrainement_etiquette.nom = "entrainement"
        entrainement_etiquette.user = seb
        entrainement_etiquette.is_checked = False

        match_etiquette.save()
        entrainement_etiquette.save()

        # Deulou match
        deuldou_match = Deuldou.objects.create(
            created_by=marie, nom="JSA", jour=datetime.now(), adresse="Salle des peupliers")
        # Deulou match2
        deuldou_match2 = Deuldou.objects.create(
            created_by=marie, nom="VS talence", jour=datetime.now(), adresse="Chez nous")
        # Deulou entrainement
        deuldou_entrainement = Deuldou.objects.create(
            created_by=marie, nom="entrainement 11 Novembre", jour=datetime.now(), adresse="Boris Diaw")
        
        # Ajouter des participants au match JSA :
        ajouter_Participant(seb.email,"seb",deuldou_match)
    
    def resultat_participants_match(self, nombre):
        un_match: Deuldou = Deuldou.objects.get(nom="JSA")
        participants = un_match.participants.all()
        print('--------- # -------------')
        print("Liste des participants : ")
        for p in participants:
            print(p)
        print('--------- Fin des participants -------------') 

        self.assertTrue(len(participants) == nombre)
    
    

    def test_ajout_participant_simple(self):
        match = Deuldou.objects.get(nom="JSA")
        # Création d'un user et ajout d'une participation :
        email = "sarah@gmail.com"
        nom = "sarah"
        ajouter_Participant(email,nom,match)
        self.assertTrue(User.objects.filter(email=email).exists())
        self.resultat_participants_match(2)
        

    def test_ajout_participant_doublon(self):
        match = Deuldou.objects.get(nom="JSA")
        # Création d'un user et ajout d'une participation :
        email = "seb@gmail.com"
        nom = "seb2"
        ajouter_Participant(email,nom,match)
        self.resultat_participants_match(1)

        
    def test_ajout_trois_contacts(self):
        """ à faire :
        ajouter 3 contacts de Marie pour le match (seb, stef, ju)
        """
        marie = User.objects.get(username="marie")
        seb_contact: Contact = Contact.objects.create(user=marie, email="seb@gmail.com", nom="seb2" )
        stef_contact: Contact = Contact.objects.create(user=marie, email="stef@gmail.com", nom="stef" )
        ju_contact: Contact = Contact.objects.create(user=marie, email="ju@gmail.com", nom="ju" )

        contacts =  Contact.objects.filter(user = marie)
        un_match: Deuldou = Deuldou.objects.get(nom="JSA")
        for contact in contacts:
            ajouter_contact_a_match(contact=contact, rdv=un_match)
        """ checker qu'au match JSA il y ait bien les 3 participants """
        self.resultat_participants_match(3)
        
    def test_ajout_liste_contacts(self):
        marie = User.objects.get(username="marie")
        stef_contact: Contact = Contact.objects.create(user=marie, email="stef@gmail.com", nom="stef" )

        liste = Liste_contacts.objects.create(user=marie, nom="match_jsa")
        liste.contacts.add(stef_contact)

        res = liste.contacts.all()
        print(res)

        
        