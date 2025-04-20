from datetime import datetime

from deuldou.models import Deuldou, Participation
from django.contrib.auth.models import User

# Création des utilisateurs
seb = User.objects.create_user(username="seb", email="seb@gmail.com", password="mdp")
seb.save()

marie = User.objects.create_user(username="marie", email="marie@gmail.com", password="mdp")
marie.save()

ju = User.objects.create_user(username="ju", email="ju@gmail.com", password="mdp")
ju.save()

# Création des doodles :
deuldou=  Deuldou(created_by=seb, nom="Ici", jour = datetime.now(), adresse="chez moi")
deuldou.save()

d2 =  Deuldou(created_by=seb, nom="maintenant", jour = datetime.now(), adresse="chez toi")
d2.save()

d3 =  Deuldou(created_by=marie, nom="chez marie", jour = datetime.now(), adresse="chez marie")
d3.save()
# création des participations :
"""
deuldou = models.ForeignKey(Deuldou, on_delete=models.CASCADE)
user = models.ForeignKey(User, on_delete=models.CASCADE)
nom = models.CharField(max_length=100, default=user)    
commentaire = models.TextField(null=True)
etiquette = models.ForeignKey(Etiquette, on_delete=models.DO_NOTHING, null=True)
statut = models.CharField(max_length=20, choices=[(x,x) for x in choix], default="pas encore participé")
visible = models.BooleanField(default=True)
"""
p1 = Participation(user=seb, deuldou=deuldou).save()
p2 = Participation(user=marie, deuldou=deuldou).save()
p3 = Participation(user=ju, deuldou=deuldou).save()
p4 = Participation(user=seb, deuldou=d2).save()
p5 = Participation(user=marie, deuldou=d2).save()
p6 = Participation(user=ju, deuldou=d2).save()
p7 = Participation(user=seb, deuldou=d3).save()

# test de contrainte : Un utilisateur ne peut pas s'inscrire 2 fois à un même doodle :
# Que faire en cas d'ajout de doublon : contrainte unique renvoie une erreur
ptest = Participation(user=ju, deuldou=d2).save()

deuldou.participants.all()

seb.deuldous.all()
seb.deuldous_crees.all()