from datetime import datetime

from deuldou.models import Deuldou, Etiquette, Invite, Liste_invitation, User
from django.core.exceptions import ObjectDoesNotExist, ValidationError

#seb = User.objects.get(username='seb')
seb = User.objects.create_user(
    username="seb", email="seb@gmail.com", password="mdp")
marie = User.objects.create_user(
    username="marie", email="marie@gmail.com", password="mdp")
ju = User.objects.create_user(
    username="ju", email="ju@gmail.com", password="mdp")
# Créationd des user supplémentaire :
sego = User.objects.create_user(
    username="sego", email="sego@gmail.com", password="mdp")
sylvain = User.objects.create_user(
    username="sylvain", email="sylvain@gmail.com", password="mdp")
amine = User.objects.create_user(
    username="Amine", email="amine@gmail.com", password="mdp")
fred = User.objects.create_user(
    username="Fred", email="fred@gmail.com", password="mdp")

# Un user invite un autre user, avec son adresse mail :
# un User crée ou a des deuldous; User sélectionne un deuldou :
# Si request.user == deuldou.created_by : Boutons d'options :
# puis Option Ajouter invité ou Liste d'invités

# fonctionnement :
# Etiquette : étiquette à mettre sur une Participation, liste appartenant au User
# insertion des étiquettes
#Etiquette.objects.create(user=seb, nom='matchs')
#Etiquette.objects.create(user=seb, nom='entrainements')
#Etiquette.objects.create(user=seb, nom='Boulot')

# Deulou match
deuldou_match = Deuldou.objects.create(
    created_by=seb, nom="JSA", jour=datetime.now(), adresse="Salle des peupliers")
# Deulou entrainement
deuldou_entrainement = Deuldou.objects.create(
    created_by=seb, nom="entrainement 11 Novembre", jour=datetime.now(), adresse="Boris Diaw")


#  insertion des invités
# invités pour les matchs
invit_ju = Invite.objects.create(
    created_by=seb, nom='ju', email='ju@gmail.com', deuldou=deuldou_match)
invit_sego = Invite.objects.create(
    created_by=seb, nom='sego', email='sego@gmail.com', deuldou=deuldou_match)
invit_sylvain = Invite.objects.create(
    created_by=seb, nom='sylvain', email='sylvain@gmail.com', deuldou=deuldou_match)
invit_marie = Invite.objects.create(
    created_by=seb, nom='marie', email='marie@gmail.com', deuldou=deuldou_match)
# invités pour test User non créé
invit_ben = Invite.objects.create(
    created_by=seb, nom='ben bob', email='benbob@gmail.com', deuldou=deuldou_match)
invit_eric = Invite.objects.create(
    created_by=seb, nom='eric', email='eric@gmail.com', deuldou=deuldou_match)
# invités pour les entrainements
invit_amine = Invite.objects.create(
    created_by=seb, nom='Amine', email='amine@gmail.com', deuldou=deuldou_entrainement)
invit_fred = Invite.objects.create(
    created_by=seb, nom='Fred', email='fred@gmail.com', deuldou=deuldou_entrainement)


# insertion des listes d'invités
Liste_invitation.objects.create(created_by=seb, nom='matchs')
Liste_invitation.objects.create(created_by=seb, nom='entrainements')

# insertion d'invités dans les listes :
matchs = Liste_invitation.objects.get(nom='matchs')
matchs.invites.add(invit_ju, invit_sego, invit_sylvain,
                   invit_marie, invit_ben, invit_eric)

# fonction d'ajout des invités :


entrainements = Liste_invitation.objects.get(nom='entrainements')
entrainements.invites.add(invit_amine, invit_fred)


"""  ******************** Requêtes SELECT *********************** """

# Envoi de la liste d'invitation sur le deuldou match :
# création de la liste en participations
# le créateur participe aussi, le rajouter (quand il crée le deuldou) !

# Voir comportement de la requête quand User n'existe pas :
# A définir :


def inviter(invite, deuldou):
    try:
        user = User.objects.get(email=invite.email)
    except ObjectDoesNotExist as e:
        # envoi d'une invitation
        print("Envoi d'une invitation à {}".format(invite.email))
        return 1
    #print("User {} existe, ajout de participation".format(user.email))
    try:
        pass
        #p = Participation(user=user, deuldou=deuldou)
        # p.full_clean()
        # p.save()
        #Participation.objects.create(user=user, deuldou=deuldou)
    except ValidationError as e:
        print(str(e))


invites = matchs.invites.all()

for invite in invites:
    inviter(invite, deuldou_match)


deuldou_match.participants.all()
