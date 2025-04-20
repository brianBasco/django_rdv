run server :
python manage.py runserver

# Création des utilisateurs avec l'API USER :

>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')


# Fonctionnement du modèle : 

Un utilisateur se log sur la page de connexion
création de compte si pas de compte

Affichage sur la page :
- de tous ses doodles :
deuldous de l'utilisateur = user.deuldous.all()

Utilisation de related-name="" pour avoir la relation inverse
relations inverse pour :
- les deuldous
- les deuldous créés
- les étiquettes (de rdv)
- les invites
- les listes d'invités

# Utiliser les tests Django :
# Définir les tests :
 - ajout d'un Rdv
 - ajout d'un user : OK
 - pas de doublon sur les users : OK
 - ajout de particpation : OK
 - pas de doublon sur les participations : OK
 

# gestion des erreurs : 
exemple : Ajout en double d'une participation : contrainte UNIQUE non respectée
Test de la méthode full_clean() sur l'instance, avant d'être .save()
La validation est bien intégrée dans le modèle directement, cool !

# fonctionnement des invitations :

Une invitation {prenom, nom, mail}
Pour chaque deuldou, un bouton d'invitation permet d'ajouter un invité/participant au deuldou
envoi de la participation :
- si l'invité n'est pas utilisateur (vérification par email) : Invitation à créer son compte :
 - Une fois le compte créé, l'invitation est supprimée de la Bdd et ajout des deuldous au User (bien vérifier tous les invités avec l'adresse mail pour ajouter les deuldous et supprimer toutes les invitations avec cette adresse mail)
- sinon le User est ajouté au deldou

Le deuldou contient une liste de participants - relation manytomany avec User
Le deuldou contient une liste d'invités - relation OneToMany avec Invite

MAJ V2 : nouveau fonctionnement :
- nouvel utilisateur sans mail d'inscription : S'inscrit normalement en passant par la page de Login
- Ajout d'un participant non inscrit comme User -> A la création du participant, Check pour savoir si le User avec cette adresse mail existe :
  - Si elle existe, le participant est déjà inscrit sur le site :
    - Envoi d'un mail d'information (Marie vous a ajouté à un Rdv)
  - sinon (le participant n'est pas inscrit) :
     - Envoi d'un mail avec lien vers page Register (avec placeholder le mail de la personne à inscrire)

### A faire :

## Trouver ou faire le mot de passe pour un auth.user
from django.contrib.auth.hashers import make_password
hashed_pass = make_password("mdp")

### Générateur de mot de passe : 
from pwgen import pwgen
pwgen()
>> '[^%6JK<&Lb}{.T#eYY+
pwgen(10, symbols=False)
>> ujr20YVkH3

# A faire :

Terminer Gestion utilisateur et mot de passe :
- checker backend mot de passe + de 8 caractères et NonNumeric entièrement : OK (avec validators de Django)
- checker backend format Email respecté : A faire
- Implémenter page de changement de mot de passe : A modifier et utiliser nouvelle fonction de validation de password
- Implémenter page de perte de mot de passe : OK 
- Refactoriser les templates : OK

- Implémenter Download .ics (avec module icalendar ou  ics) : OK

- Corriger l'ajout du User en PArticipant à un rdv (nom = null pour l'instant) :OK Fait
  
- Finir le formulaire d'ajout d'un rdv avec les erreurs : OK fait

- tests à faire :
  - permission de créer rdv : Fait
  - Ne pas ajouter de particpant à un rdv d'un autre user : Fait par erreur 403
  - Ne pas accéder aux Contacs d'un autre user : OK (Filter = User) donc pas possible d'usurper User
  - Ne pas accéder aux Rdv des autres user (ajout, modification, suppression):
  - Ne pas accéder aux Participants des autres user (ajout, modification, suppression):
  - Ne pas accéder aux profils des autres user (ajout, modification, suppression):
  - Création de participants en double : Fait
  - Checker création de contact en double pour un User : OK Fait
  - Ne pas ajouter un Participant sans rentrer une adresse mail valide : OK fait Fait en modificant le Model (EmailField)
  - Redéfinir en français les erreurs sur les formulaires :

- Implémenter page des contacts : FAIT (retravailler UI liste de contacts dans le formulaire)
- Implémenter PWA
- implémenter SSO (facultatif)
- Implémenter i18n
- Changer le STATIC en mode production


Infos sur gestion des mots de passe en Django :
https://lasteminista.com/reinitialisation-du-mot-de-passe-authentification-django-2-partie/
https://pylessons.com/django-handle-password (avec vidéo)

Portail Administrateur :
path('admin/', admin.site.urls)

Forms :
tweaking des inputs : django-widget-tweaks
https://pypi.org/project/django-widget-tweaks/

## App Contacts

Ajout d'une app Contacts sur le projet, permettant d'ajouter les contacts depuis l'api de Google People

Connexion à l'api grâce à Google Cloud et le projet rdvs, ajout du fichier avec les credentials à la racine de ce projet. (contacts_client_secret.json)
Ajout des codes dans les Settings du projet Django

## A faire :

App registration : fonctionnel (27/02/2025)
Télécharger Calendrier par Rdv 