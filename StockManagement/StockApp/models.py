from django.db import models
from django.shortcuts import render
#from django.contrib.auth.models import User


class RawMaterial(models.Model):
    mass_vol=(
        ('kg','KiloGrams'),
        ('ltr','Litres'),
    )
    name=models.CharField(max_length=500, verbose_name='Raw-Material-Name', default=None)
    date=models.DateField(verbose_name='raw-material_date', auto_now=True)
    raw_cat=models.CharField(max_length=350)
    raw_sub_cat=models.CharField(max_length=300)
    quantity=models.FloatField(verbose_name='raw_material_quantity')
    mode=models.CharField(max_length=120, choices=mass_vol)
    density=models.FloatField(verbose_name='raw-material_denisty')
    selected=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ProductionStage(models.Model):
    prod_form=(
        ('ink','ink'),
        ('paint','paint'),
    )
    date_prod=models.DateField(verbose_name='production_date', auto_now=True)
    raw_material=models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    name=models.CharField(max_length=350, verbose_name='product name')
    quantity_prod=models.FloatField(verbose_name='ProdutionQuantity')
    #ratio1=models.IntegerField(verbose_name='ratio1', default=0)
    #ratio2=models.IntegerField(verbose_name='ratio2', default=0)
    #ratio3=models.IntegerField(verbose_name='ratio3', default=0)
    selected=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Dispatch(models.Model):
    date_dispatch=models.DateField(verbose_name='date_of_dispatch', auto_now=True)
    product=models.ForeignKey(ProductionStage,on_delete=models.CASCADE)
    bill_no=models.IntegerField(verbose_name='bill_number')
    dispatch_status=models.BooleanField(default=True)

    def __str__(self):
        return self.bill_no




# Create your models here.
