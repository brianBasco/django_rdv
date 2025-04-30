from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .models import Contact, Deuldou, ListeContacts, Participant


# Rdv Form V2
class RdvForm(forms.ModelForm):
    class Meta:
        model = Deuldou
        fields = ['nom','jour','heure_debut','heure_fin','lieu']

    def clean(self):
        cleaned_data = super().clean()
        fin = cleaned_data.get("heure_fin")
        debut = cleaned_data.get("heure_debut")

        if fin is None :
            cleaned_data["heure_fin"] = '00:00'

        if debut is None :
            cleaned_data["heure_debut"] = '00:00'



class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ["rdv", "email", "nom"]
        widgets = {'rdv': forms.HiddenInput()}

        error_messages = {
            "email": {
                "required": _("L'émail est obligatoire"),
            },
            "nom": {
                "required": _("Un nom est obligatoire"),
            },
        }
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        rdv = self.cleaned_data["rdv"]
        if Participant.objects.filter(email=email, rdv=rdv).exists():
            raise ValidationError("{} est déjà enregistré pour ce Rendez-vous".format(email))
        return email


# Formulaire à renommer -> ParticipantUpdate
"""
class UpdateParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ["nom","statut"]
"""
class UpdateParticipantForm(ParticipantForm):
    class Meta(ParticipantForm.Meta):
        fields = ["nom","statut"]


class SelectContactForm(forms.Form):
    """
    Formulaire pour ajouter des Contacts comme participants à un rendez-vous
    """
    email = forms.EmailField(widget=forms.HiddenInput())
    nom = forms.CharField(widget=forms.HiddenInput())#label=""
    is_checked = forms.BooleanField(required=False, initial=False,label="")

    is_checked.widget.attrs.update({"class": "form-check-input form-check-input-perso"})


# -------------- Formulaire pour la gestion des contacts --------------

class ContactForm(forms.ModelForm):
    """
    Formulaire de création d'un contact
    au 30/04/2025 : à améliorer : Supprimer le widget user et passer le paramètre user à l'instanciation (comme pour les listes de contacts)
    """
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {'user': forms.HiddenInput()}
    
    
# -------------- Formulaire pour le groupe de contacts --------------
# permet de créer un groupe de contacts
# permet de modifier le nom du groupe de contacts
# permet d'ajouter des contacts du user
# permet de supprimer des contacts du user

class ListeContactsForm(forms.ModelForm):
    """
    Formulaire de création d'un groupe de contacts
    Attribut obligatoire à passer à l'instanciation : user
    Contrainte de nom unique pour un utilisateur
    """
    class Meta:
        model = ListeContacts
        fields= ['nom','contacts']
        widgets = {'contacts': forms.CheckboxSelectMultiple(), 'nom': forms.TextInput(attrs={'class': "form-control",'placeholder': "Nom du groupe"})}
        error_messages = {
            "nom": {
                "required": _("Un nom est obligatoire"),
            },
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Récupère l’utilisateur passé depuis la vue
        super().__init__(*args, **kwargs)
        self.user = user  # Stocke l’utilisateur dans l’instance du formulaire
         # Ne tente de modifier le queryset que si le champ 'contacts' est présent dans le formulaire
        if not user:
            raise Exception("Le paramètre user doit être spécifié à l'initialisation du formulaire")
        if 'contacts' in self.fields:
                self.fields['contacts'].required = False
                self.fields['contacts'].queryset = Contact.objects.filter(user=user)
    
    def clean_nom(self):
        nom = self.cleaned_data["nom"]
        if ListeContacts.objects.filter(nom=nom, user=self.user).exists():
            raise ValidationError("{} : Ce nom existe déjà !".format(nom))
        return nom
    


class UpdateNomListeContactForm(ListeContactsForm):
    """
    Formulaire dérivé pour modifier uniquement le nom d'une liste de contacts.
    Attribut obligatoire à passer à l'instanciation : user (pour la contrainte d'unicité)
    """

    class Meta(ListeContactsForm.Meta):
        fields = ['nom']  # On limite le champ éditable à 'nom'



class AjouterContactsForm(forms.ModelForm):
    """
    Formulaire pour ajouter des contacts à une liste existante.
    Seuls les contacts de l'utilisateur qui ne sont pas déjà dans la liste sont proposés.
    """
    class Meta:
        model = ListeContacts
        fields = ['contacts']
        widgets = {
            'contacts': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        liste = kwargs.pop('liste', None)  # la liste à laquelle on veut ajouter des contacts
        super().__init__(*args, **kwargs)
        self.fields['contacts'].required = False

        if user and liste:
            contacts_exclus = liste.contacts.all()
            self.fields['contacts'].queryset = Contact.objects.filter(user=user).exclude(id__in=contacts_exclus)
        else:
            self.fields['contacts'].queryset = Contact.objects.none()