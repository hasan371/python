from rest_framework import serializers
from sapt.models import *


class serialmodl(serializers.ModelSerializer):
    class Meta:
        model = sapt
        fields = '__all__'


class serialget(serializers.Serializer):
    meli = serializers.CharField(max_length=10)
    nameandfamily = serializers.CharField(max_length=150)
    tarmoraje = serializers.DateField()
    taraz = serializers.DateField()
    tarta = serializers.DateField()
    kolestarhat = serializers.IntegerField()
    estarhattaednashodeh = serializers.IntegerField()
    shsapt = serializers.IntegerField()