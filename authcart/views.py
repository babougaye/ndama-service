from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
#from .utils import generate_token
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.conf import settings
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
User = get_user_model()




#def inscrire(request):
    #if request.method == "POST":
        #email = request.POST['email']
        #password = request.POST['passe1']
        #confirme_password = request.POST['passe2']

       # if password != confirme_password:
           # messages.warning(request, "Le mot de passe ne correspond pas")
           # return redirect('inscrire')

        #if User.objects.filter(username=email).exists():
            #messages.info(request, "Cet email est déjà utilisé")
            #return redirect('inscrire')

        #user = User.objects.create_user(email, email, password=password)
        #user.is_active = False
        #user.save()

        #messages.success(request, "Utilisateur créé avec succès")
        #return redirect('/auth/connexion/')

    #return render(request, "inscrire.html")
#def connexion(request):
    #if request.method == "POST":
       # email = request.POST.get('email')
        #password = request.POST.get('passe1')

        #user = authenticate(request, username=email, password=password)
        #if user is not None:
            #if user.is_active:
                #login(request, user)
                #messages.success(request, "Connexion réussie")
                #return redirect("/")
            #else:
               # messages.warning(request, "Votre compte n'est pas encore activé. Veuillez vérifier votre email pour l'activer.")
        #else:
           # messages.error(request, "Identifiants invalides. Veuillez réessayer.")

        #return redirect('/auth/connexion/')

    #return render(request, 'connexion.html')


#def deconnexion(request):
    #logout(request)
    #messages.success(request, "Déconnexion réussie")
    #return redirect('/auth/connexion/')
