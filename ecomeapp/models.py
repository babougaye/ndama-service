from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField(max_length=500)
    telephone = models.CharField(max_length=15)  # Changer en CharField pour inclure les codes pays et éviter les limites des entiers

    def __str__(self):
        return self.name

class Produit(models.Model) :
    produit_id = models.AutoField
    produit_name=models.CharField(max_length=100) 
    categorie=models.CharField(max_length=100,default="")
    subcategorie=models.CharField(max_length=50,default="")
    prix = models.IntegerField(default=0)  # Correction du champ pour le prix
    desc=models.CharField(max_length=300)
    
    image = models.ImageField(upload_to='images/images')
    
    def __str__(self):
        return self.produit_name
  
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
   
    email = models.EmailField(max_length=90)
    name = models.CharField(max_length=90)
    addresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    pays = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, default="")

    def __str__(self):
        return f"Order {self.order_id} - {self.name}"
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)
    update_message = models.CharField(max_length=255, default="Commande reçue")  # Ajoute une valeur par défaut ici

    def __str__(self):
        return f"Order {self.order.order_id} - Delivered: {self.delivered} on {self.timestamp}"


class Categorie(models.Model) :
    produit_id = models.AutoField
    produit_name=models.CharField(max_length=100) 
    categorie=models.CharField(max_length=100,default="")
    subcategorie=models.CharField(max_length=50,default="")
    prix = models.IntegerField(default=0)  # Correction du champ pour le prix
    desc=models.CharField(max_length=300)
    
    image = models.ImageField(upload_to='images/images')
    
    def __str__(self):
        return self.produit_name
    

    