from django.contrib import admin
from ecomeapp.models import Contact,Produit,Orders,OrderUpdate,Categorie

# Register your models here.
admin.site.register(Contact),
admin.site.register(Produit)
admin.site.register(Orders),
admin.site.register(OrderUpdate)
admin.site.register(Categorie)