from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    #path('', views.login_view, name='login'),
    path('login', views.login_view, name="login"),
    path('registration', views.registration, name="registration"),
    #path('modifier_password', views.modifier_password, name="modifier_password"),
    path('logout', views.logout_view, name="logout"),

    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name="password_reset_complete"),
]