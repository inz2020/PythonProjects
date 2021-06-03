from rest_framework import serializers
from buildrzapi.models import Parcelle, Parcelle

class ParcelleSerializer(serializers.ModelSerializer):
    class Meta:
        model =Parcelle
        fields = '__all__'