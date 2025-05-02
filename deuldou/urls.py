from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.connexion, name="connexion"),

    
    # path('login', views.login_view, name="login"),
    # path('registration', views.registration, name="registration"),
    # path('modifier_password', views.modifier_password, name="modifier_password"),
    # path('logout', views.logout_view, name="logout"),
    
    
    # path('add_contact', views.add_contact_view, name="add_contact"),
    #path('add_liste_contact', views.add_liste_contact_view,name="add_liste_contact"),

    

    # fonctions de la page 0 :
    path('', views.home_view, name="home"),
    path('x_addRdv', views.x_addRdv, name="x_addRdv"),
    path('x_getRdvs', views.x_get_my_rdvs, name="x_getRdvs"),
    path('x_get_my_anciens_rdvs', views.x_get_my_anciens_rdvs, name="x_get_my_anciens_rdvs"),
    path('htmx_updateParticipant/<int:id_participant>',
         views.x_updateMyParticipation, name="htmx_updateParticipant"),
    path('htmx_getParticipants/<int:id_rdv>',
         views.x_getParticipants, name="htmx_getParticipants"),

    # fonctions de la page 1 :
    path('gerer_rdvs', views.gerer_rdvs_view, name="gerer_rdvs"),  # Secu OK
    path('x_get_rdvs', views.x_get_rdvs, name="x_get_rdvs"),  # Secu OK
    path('x_update_rdv/<int:id>', views.x_update_rdv, name="x_update_rdv"),
    path('deleteRdv/<int:rdv_id>', views.x_deleteRdv, name="x_deleteRdv"),
    path('x_addParticipant/<int:rdv_id>',
         views.x_addParticipant, name="x_addParticipant"),
    path('x_gestion_getParticipants/<int:rdv_id>',
         views.x_gestion_getParticipants, name="x_gestion_getParticipants"),
    path('x_deleteParticipant/<int:id>',
         views.x_deleteParticipant, name="x_deleteParticipant"),
    path('x_selectContacts/<int:rdv_id>', views.x_selectContacts, name="x_selectContacts"),

     # fonctions de la page Contacts :
     path('contacts', views.contacts_view, name="contacts"),
     path('x_getContacts', views.x_getContacts, name="x_getContacts"),
     path('x_addContact', views.x_addContact, name="x_addContact"),
     path('x_updateContact/<int:contact_id>', views.x_updateContact, name="x_updateContact"),
     path('x_deleteContact/<int:contact_id>', views.x_deleteContact, name="x_deleteContact"),
     ### Partie Listes de contacts :
     path('x_addGroupeContacts', views.x_addGroupeContacts, name="x_addGroupeContacts"),
     path('x_getListesContacts', views.x_getListesContacts, name="x_getListesContacts"),
     path('x_getGroupeContacts/<int:groupe_id>', views.x_getGroupeContacts, name="x_getGroupeContacts"),
     path('x_updateListeContacts/<int:liste_id>', views.x_updateListeContacts, name="x_updateListeContacts"),
     path('x_deleteListeContacts/<int:liste_id>', views.x_deleteListeContacts, name="x_deleteListeContacts"),
     path('x_addContactsToGroupe/<int:liste_id>', views.x_addContactsToGroupe, name="x_addContactsToGroupe"),
     path('x_deleteContactsFromGroupe/<int:liste_id>', views.x_deleteContactsFromGroupe, name="x_deleteContactsFromGroupe"),
     

     # fonctions du iCal :
    path('download_cal/<int:rdv_id>', views.download_cal , name="download_cal"),


    # vue des tests
    path('test', views.test, name="test"),
    #path('test_download', views.test_download, name="test_download"),
    path('test_oob', views.test_oob, name="test_oob"),
    path('test_index', views.test_index, name="test_index"),


    # Vue des components
    path('rdv_template', views.rdv_template, name="rdv_template"),

    

]

# handler404 = 'mysite.views.my_custom_page_not_found_view'
