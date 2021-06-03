from rest_framework import viewsets
from  buildrzapi import models
from  buildrzapi import serializers

class ParcelleViewset(viewsets.ModelViewSet):
    queryset = models.Parcelle.objects.all()
    serializer_class = serializers.ParcelleSerializer