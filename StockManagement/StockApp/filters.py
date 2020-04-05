import django_filters
from .models import RawMaterial

class RawMaterialFilter(django_filters.FilterSet):
    
    class Meta:
        model=RawMaterial
        fields=[
            'name',
            'mode',
            'raw_cat',
            'raw_sub_cat',
        ]