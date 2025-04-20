from datetime import datetime

from deuldou.models import Deuldou, Etiquette, Invite, Liste_invitation, User
from django.core.exceptions import ObjectDoesNotExist, ValidationError

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

# Deulou match
deuldou_match = Deuldou.objects.create(
    created_by=marie, nom="JSA", jour=datetime.now(), adresse="Salle des peupliers")
# Deulou match2
deuldou_match2 = Deuldou.objects.create(
    created_by=marie, nom="VS talence", jour=datetime.now(), adresse="Chez nous")
# Deulou entrainement
deuldou_entrainement = Deuldou.objects.create(
    created_by=marie, nom="entrainement 11 Novembre", jour=datetime.now(), adresse="Boris Diaw")

# deuldou.invites.all()
sebInvite = Invite()
sebInvite.email = "seb@gmail.com"
sebInvite.deuldou = deuldou_match
sebInvite.invited_by = marie
sebInvite.save()

seb2Invite = Invite()
seb2Invite.email = "seb@gmail.com"
seb2Invite.deuldou = deuldou_match2
seb2Invite.invited_by = marie
seb2Invite.save()

juInvite = Invite()
juInvite.email = "ju@gmail.com"
juInvite.deuldou = deuldou_match
juInvite.invited_by = marie
juInvite.save()

segoInvite = Invite()
segoInvite.email = "sego@gmail.com"
segoInvite.deuldou = deuldou_match
segoInvite.invited_by = marie
segoInvite.save()

# Eric est invité au match mais pas inscrit :
ericInvite = Invite()
ericInvite.email = "eric@gmail.com"
ericInvite.deuldou = deuldou_match
ericInvite.invited_by = marie
ericInvite.save()
