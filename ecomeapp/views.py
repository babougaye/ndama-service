from decimal import Decimal, InvalidOperation
from django.shortcuts import render, redirect
from ecomeapp.models import Contact, Produit, Orders, OrderUpdate
from django.contrib import messages
from math import ceil
from decimal import Decimal, InvalidOperation
from .models import Orders, OrderUpdate
from django.http import JsonResponse

def index(request):
    allProds = []
    catprods = Produit.objects.values('categorie', 'id')
    cats = {item['categorie'] for item in catprods}
    for cat in cats:
        prod = Produit.objects.filter(categorie=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, "index.html", params)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        number = request.POST.get("number")
        myquery = Contact(name=name, email=email, desc=desc, telephone=number)
        myquery.save()
        messages.info(request, "Nous reviendrons vers vous bientôt.")
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def checkout(request):
    #if not request.user.is_authenticated:
        #messages.warning(request, "Veuillez vous connecter avant de passer commande.")
        #return redirect('auth/connexion')

    if request.method == "POST":
        items_json = request.POST.get("items_json", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        amount_str = request.POST.get("amt", "0").strip()
        addresse = request.POST.get("addresse", "")
        ville = request.POST.get("ville", "")
        pays = request.POST.get("pays", "")
        zip_code = request.POST.get("zip_code", "")
        phone = request.POST.get("phone", "")

        # Remplacer les virgules par des points si nécessaire
        amount_str = amount_str.replace(',', '.')

        # Conversion de l'amount en Decimal
        try:
            amount = Decimal(amount_str)
        except (ValueError, InvalidOperation) as e:
            messages.error(request, f"Montant invalide : '{amount_str}'")
            return JsonResponse({'success': False, 'message': 'Montant invalide.'})

        # Si tout est correct, on peut créer la commande
        order = Orders(
            name=name, 
            email=email, 
            items_json=items_json, 
            amount=amount,
            addresse=addresse, 
            ville=ville,
            pays=pays,
            zip_code=zip_code,
            phone=phone,
        )
        order.save()

        update = OrderUpdate(
            order=order,  
            update_message="La commande a été passée"
        )
        update.save()

        messages.success(request, "Votre commande a été passée avec succès.")
        return JsonResponse({'success': True, 'message': 'Votre commande a été passée avec succès.'})

    return render(request, "checkout.html")

def block(request):
    return render(request, "block.html")


def categorie(request):
    
    allProds = []
    catprods = Produit.objects.values('categorie', 'id')
    cats = {item['categorie'] for item in catprods}
    for cat in cats:
        prod = Produit.objects.filter(categorie=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, "categorie.html", params)
    

def service(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Connectez-vous et réessayez.")
       # return redirect('auth/connexion')
    currentuser=request.user.username
    items = Orders.objects.filter(email=currentuser)
    for i in items:
        print(i.order_id)
    context = {"items":items}
    print(currentuser)
    return render(request, "service.html",context)


def recherche(request):
    query = request.GET.get('q', '')  # 'name' est remplacé par le champ correct
    if query:
        produits = Produit.objects.filter(produit_name__icontains=query)
    else:
        produits = Produit.objects.none()
    return render(request, 'recherche.html', {'produits': produits, 'query': query})