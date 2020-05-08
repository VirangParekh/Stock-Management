from django.contrib import admin
from .models import RawMaterial,ProductionStage,Dispatch

# Register your models here.
admin.site.register(RawMaterial)
admin.site.register(ProductionStage)
admin.site.register(Dispatch)
