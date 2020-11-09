from django.db import models

# Create your models here.
class sapt(models.Model):
    meli = models.CharField(max_length=10)
    nameandfamily = models.CharField(max_length=150)
    father = models.CharField(max_length=100)
    ozviat = models.CharField(max_length=15)
    nosazman = models.CharField(max_length=15)
    mahalkhedmat = models.CharField(max_length=150)
    nobimari = models.CharField(max_length=150)
    vaziatbimari = models.CharField(max_length=10)
    noestarhat = models.CharField(max_length=10)
    tarmoraje = models.DateField()
    taraz = models.DateField()
    tarta = models.DateField()
    kolestarhat = models.IntegerField()
    estarhattaednashodeh = models.IntegerField()
    pezeshmktaed = models.CharField(max_length=100)
    shsapt = models.IntegerField()
    pezeshkmoalej = models.CharField(max_length=100)

    def __str__(self):
        return self.meli