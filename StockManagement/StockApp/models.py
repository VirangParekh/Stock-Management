from django.db import models
from django.shortcuts import render
#from django.contrib.auth.models import User
from datetime import datetime
from django.utils.translation import ugettext_lazy as _


class RawMaterial(models.Model):
    mass_vol = (
        ('kg', 'KiloGrams'),
        ('ltr', 'Litres'),
    )
    name = models.CharField(
        max_length=500, verbose_name='Raw-Material-Name', default=None)
    date = models.DateField(verbose_name='raw-material_date')
    # raw_cat=models.CharField(max_length=350)
    quantity = models.FloatField(verbose_name='raw_material_quantity')
    mode = models.CharField(max_length=120, choices=mass_vol)
    density = models.FloatField(verbose_name='raw-material_denisty')
    selected = models.BooleanField(default=False)
    rate = models.FloatField(verbose_name='raw_material_rate')
    supplier = models.CharField(verbose_name='supplier_name', max_length=300)

    class Meta:
        verbose_name = _('raw material')
        verbose_name_plural = _('raw materials')
        ordering = (
            'date',
            'name',
            'quantity',
        )

    def __str__(self):
        return self.name


class ProductionStage(models.Model):
    date_prod = models.DateField(verbose_name='production_date')
    raw_materials = models.ManyToManyField(RawMaterial)
    name = models.CharField(max_length=350, verbose_name='product name')
    quantity_prod = models.FloatField(verbose_name='ProdutionQuantity')
    quantity1 = models.FloatField(verbose_name='Quantity 1')
    quantity2 = models.FloatField(verbose_name='Quantity 2')
    quantity3 = models.FloatField(verbose_name='Quantity 3')
    quantity4 = models.FloatField(verbose_name='Quantity 4')
    quantity5 = models.FloatField(verbose_name='Quantity 5')
    quantity6 = models.FloatField(verbose_name='Quantity 6')
    quantity7 = models.FloatField(verbose_name='Quantity 7')
    selected = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = (
            'date_prod',
            'name',
            'quantity_prod',
        )


class Dispatch(models.Model):
    date_dispatch = models.DateField(verbose_name='date_of_dispatch')
    products = models.ManyToManyField(to=ProductionStage)
    bill_no = models.IntegerField(verbose_name='bill_number')
    quantity1 = models.FloatField(verbose_name='Quantity 1')
    quantity2 = models.FloatField(verbose_name='Quantity 2')
    quantity3 = models.FloatField(verbose_name='Quantity 3')
    quantity4 = models.FloatField(verbose_name='Quantity 4')
    quantity5 = models.FloatField(verbose_name='Quantity 5')
    quantity6 = models.FloatField(verbose_name='Quantity 6')
    quantity7 = models.FloatField(verbose_name='Quantity 7')
    dispatch_status = models.BooleanField(
        verbose_name='dispatch_status', default=True)

    class Meta:
        verbose_name = _('dispatch')
        verbose_name_plural = _('dispatches')
        ordering = (
            'date_dispatch',
            'bill_no',
        )

    def __str__(self):
        return str(self.bill_no)

# Create your models here.
