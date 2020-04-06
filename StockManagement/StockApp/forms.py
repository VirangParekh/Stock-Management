from django import forms
from .models import RawMaterial, ProductionStage, Dispatch
from django.contrib.auth.models import User

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

""" class LoginForm(forms.ModelForm):

    class Meta:
        model=User
        fields=[
            'username',
            'password',
        ] """

