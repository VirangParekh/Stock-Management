from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import User


class RawMaterial(models.Model):
    mass_vol=(
        ('kg','KiloGrams'),
        ('ltr','Litres'),
    )
    date=models.DateField(verbose_name='raw-material_date', auto_now=True)
    raw_cat=models.CharField(max_length=350)
    raw_sub_cat=models.CharField(max_length=300)
    quantity=models.FloatField(verbose_name='raw_material_quantity')
    mode=models.CharField(max_length=120, choices=mass_vol)
    density=models.FloatField(verbose_name='raw-material_denisty')


class ProductionStage(models.Model):
    prod_form=(
        ('ink','ink'),
        ('paint','paint'),
    )
    date_prod=models.DateField(verbose_name='production_date', auto_now=True)
    raw_material=models.ForeignKey(RawMaterial, on_delete=models.CASCADE)
    name=models.CharField(max_length=350, verbose_name='product name')
    quantity_prod=models.FloatField(verbose_name='ProdutionQuantity')

class Dispatch(models.Model):
    date_dispatch=models.DateField(verbose_name='date_of_dispatch')
    product=models.ForeignKey(ProductionStage,on_delete=models.CASCADE)
    bill_no=models.IntegerField(verbose_name='bill_number')
    dispatch_status=models.BooleanField(default=True) 




# Create your models here.
