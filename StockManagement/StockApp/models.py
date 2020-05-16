from django.db import models
from django.shortcuts import render
#from django.contrib.auth.models import User
from datetime import datetime


class RawMaterial(models.Model):
    mass_vol=(
        ('kg','KiloGrams'),
        ('ltr','Litres'),
    )
    name=models.CharField(max_length=500, verbose_name='Raw-Material-Name', default=None)
    date=models.DateField(verbose_name='raw-material_date')
    raw_cat=models.CharField(max_length=350)
    quantity=models.FloatField(verbose_name='raw_material_quantity')
    mode=models.CharField(max_length=120, choices=mass_vol)
    density=models.FloatField(verbose_name='raw-material_denisty')
    selected=models.BooleanField(default=False)
    rate=models.FloatField(verbose_name='raw_material_rate')
    supplier=models.CharField(verbose_name='supplier_name', max_length=300)

    '''@classmethod
    def from_db(self, )'''

    def __str__(self):
        return self.name

class ProductionStage(models.Model):
    date_prod=models.DateField(verbose_name='production_date')
    raw_material=models.ManyToManyField(RawMaterial)
    name=models.CharField(max_length=350, verbose_name='product name')
    quantity_prod=models.FloatField(verbose_name='ProdutionQuantity')
    selected=models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)

class Dispatch(models.Model):
    date_dispatch=models.DateField(verbose_name='date_of_dispatch')
    product=models.ManyToManyField(to=ProductionStage)
    bill_no=models.IntegerField(verbose_name='bill_number')
    dispatch_status=models.BooleanField(verbose_name='dispatch_status', default=True)


    def __str__(self):
        return str(self.bill_no)

# Create your models here.
