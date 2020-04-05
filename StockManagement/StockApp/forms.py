from django import forms
from .models import RawMaterial, ProductionStage, Dispatch

class RawMaterialForm(forms.ModelForm):

    class Meta:
        model=RawMaterial
        fields='__all__'


class ProductionStageForm(forms.ModelForm):

    class Meta:
        model=ProductionStage
        fields='__all__'

class DispatchForm(forms.ModelForm):

    class Meta:
        model=Dispatch
        fields='__all__'

