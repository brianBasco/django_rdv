from django.forms import ValidationError
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import (MinimumLengthValidator,
                                                     NumericPasswordValidator)
from django.contrib.auth.models import User

from apps.registration.services.utils import check_passwordValidation

"""
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige vers une page d'accueil
        else:
            messages.error(request, 'Identifiants invalides')
    return render(request, 'login.html')

"""

# ------------------- Vues de Connexion/Déconnexion  ---------------------
def login_view(request: HttpRequest):

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            print("user identifié !!")
            # Redirect to a success page.
            login(request, user)
            return redirect('home')

        else:
            messages.add_message(
                request, messages.ERROR, "Erreur lors de la connexion - Identifiants incorrects")
            return render(request, 'login.html')

    return render(request, 'login.html')


def registration(request: HttpRequest):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        nom = request.POST['nom']

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR,
                                 'Cet utilisateur existe déjà')

        elif check_passwordValidation(request, password):
            user = User.objects.create_user(
                username=email, email=email, password=password, first_name=nom)
            login(request, user)
            return redirect('home')
    return render(request, 'register.html')


@login_required
def logout_view(request: HttpRequest):
    messages.add_message(request, messages.INFO, 'Déconnexion ! @Bientôt')
    logout(request)
    # Redirect to a success page.
    return redirect('login')

# ------------------- Fin des Vues de Connexion/Déconnexion  ---------------------


"""
def __check_passwordValidation(request: HttpRequest, password: str):
    validators = [MinimumLengthValidator, NumericPasswordValidator]
    try:
        for validator in validators:
            validator().validate(password)
        return True
    except ValidationError as e:
        messages.add_message(request, messages.ERROR, str(e))
        return False

"""
