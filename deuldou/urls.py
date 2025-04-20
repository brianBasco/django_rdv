from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.connexion, name="connexion"),
    path('', views.home, name="home"),

    
    # path('login', views.login_view, name="login"),
    # path('registration', views.registration, name="registration"),
    # path('modifier_password', views.modifier_password, name="modifier_password"),
    # path('logout', views.logout_view, name="logout"),
    
    
    path('contacts', views.contacts_view, name="contacts"),
    # path('add_contact', views.add_contact_view, name="add_contact"),
    #path('add_liste_contact', views.add_liste_contact_view,name="add_liste_contact"),

    # fonctions du iCal :
    path('download_cal/<int:rdv_id>', views.download_cal , name="download_cal"),

    # fonctions de la page 0 :
    path('x_addRdv', views.x_addRdv, name="x_addRdv"),
    path('x_getRdvs', views.x_getRdvs, name="x_getRdvs"),
    path('htmx_updateParticipant/<int:id_participant>',
         views.htmx_updateParticipant, name="htmx_updateParticipant"),
    path('htmx_getParticipants/<int:id_rdv>',
         views.htmx_getParticipants, name="htmx_getParticipants"),

    # fonctions de la page 1 :
    path('gerer_rdvs', views.gerer_rdvs, name="gerer_rdvs"),  # Secu OK
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
     path('x_getContacts', views.x_getContacts, name="x_getContacts"),
     path('x_addContact', views.x_addContact, name="x_addContact"),
     path('x_updateContact/<int:contact_id>', views.x_updateContact, name="x_updateContact"),
     path('x_deleteContact/<int:contact_id>', views.x_deleteContact, name="x_deleteContact"),
     ### Partie Listes de contacts :
     path('x_addListeContacts', views.x_addListeContacts, name="x_addListeContacts"),
     path('x_getListesContacts', views.x_getListesContacts, name="x_getListesContacts"),
     path('x_updateListeContacts/<int:liste_id>', views.x_updateListeContacts, name="x_updateListeContacts"),
     path('x_deleteListeContacts/<int:liste_id>', views.x_deleteListeContacts, name="x_deleteListeContacts"),


    # vue des tests
    path('test', views.test, name="test"),
    #path('test_download', views.test_download, name="test_download"),
    path('test_oob', views.test_oob, name="test_oob"),
    path('test_index', views.test_index, name="test_index"),

    

    # fonctions de la page Profil :
    path('x_get_profil', views.x_get_profil, name="x_get_profil"),    

    # Vue des components
    path('rdv_template', views.rdv_template, name="rdv_template"),

    

]

# handler404 = 'mysite.views.my_custom_page_not_found_view'
