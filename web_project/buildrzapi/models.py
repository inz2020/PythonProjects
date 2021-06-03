from django.db import models

# Create your models here.

class Parcelle(models.Model):

    idParcelle=models.CharField(max_length=100)
    adresse= models.CharField(max_length=200)
    codePostal= models.CharField(max_length=200)
    ville= models.CharField(max_length=200)
    surface= models.CharField(max_length=200)
    adresse= models.CharField(max_length=200)


   # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE


