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

"""
class UpdateRdvForm(RdvForm):
    class Meta:
        exclude = [""]
        fields = ['nom','jour','heure_debut','heure_fin','lieu']
"""

    
    
"""
class Add_Participant_Form(forms.Form):
    email = forms.EmailField(max_length=100)
    nom = forms.CharField(max_length=100)
    statut= forms.CharField(max_length=2,widget=forms.Select(choices=Participant.STATUTS_CHOICES))
"""


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


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {'user': forms.HiddenInput()}

    def clean_email(self):
        email = self.cleaned_data["email"]
        user  = self.cleaned_data["user"]
        if Contact.objects.filter(email=email, user=user).exists():
            raise ValidationError("{} est déjà enregistré dans vos contacts".format(email))
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return email



class ListeContactsForm(forms.ModelForm):
    class Meta:
        model = ListeContacts
        fields= ['user','nom','contacts']
        widgets = {'user': forms.HiddenInput(), 'contacts': forms.CheckboxSelectMultiple(attrs={'required': False}), 'nom': forms.TextInput(attrs={'class': "form-control"})}


class SelectContactForm(forms.Form):
    #class Meta(ContactForm.Meta):
    #   widgets = {'user': forms.HiddenInput(),'email': forms.HiddenInput()}
    email = forms.EmailField(widget=forms.HiddenInput())
    nom = forms.CharField(widget=forms.HiddenInput())#label=""
    is_checked = forms.BooleanField(required=False, initial=False,label="")

    is_checked.widget.attrs.update({"class": "form-check-input form-check-input-perso"})
    #nom.widget.attrs.update({"class": "form-control-plaintext"})
