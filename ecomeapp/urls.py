from django.urls import path
from ecomeapp import views


urlpatterns = [
 path('', views.index,name="index"),
 path('contact', views.contact,name="contact"),
 path('categorie/', views.categorie,name="categorie"),
 path('service/', views.service,name="service"),
 path('checkout/', views.checkout,name="checkout"),
 path('recherche/', views.recherche, name='recherche'),
 
 path('about', views.about,name="about")
    
]
