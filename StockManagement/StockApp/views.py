from django.shortcuts import render
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, Page
#import templates.virang_templates

class RawMaterialDisplayView(ListView):
    model=RawMaterial
    context_object_name='view_raw_material'
    queryset=RawMaterial.objects.all()
    paginate_by=5


    def get_context_data(self,**kwargs):
        self.context_object_name=super(RawMaterialDisplayView, self).get_context_data(**kwargs)
        self.context_object_name['number']=self.paginate_by
        #self.context_object_name['expand']=self.expand_raw_material(name=name)
        return self.context_object_name

    #template_name='StockApp/rawmaterial_list.html'

class RawMaterialCreateView(CreateView):
    model=RawMaterial
    fields='__all__'
    template_name='StockApp/rawmaterial_create.html'
    success_url='/view_raw_material'

    def change_rate(self):
        if self.object is not None:
            mode=getattr(self.object,'mode')
            quantity=getattr(self.object,'quantity')
            if mode=='ltr':
                density=getattr(self.object,'density')
                rate=getattr(self.object,'density')
                rate=rate*density
                self.object.rate=rate
                self.object.save()
            else:
                pass


def expand_raw_material(request,name):
    raw_material=RawMaterial.objects.filter(name=name)
    print(type(RawMaterial))
    expand=[]
    for i in raw_material:
        supplier=getattr(i, 'supplier')
        quantity=getattr(i, 'quantity')
        date=getattr(i,'date')
        expand.append([name,supplier,quantity,date])
    return expand


class ExpandRawMaterialView(ListView):
    model=RawMaterial
    context_object_name='expand_raw_material'
    template_name='StockApp/expand_list.html'
    
    def get_queryset(self, **kwargs):
        return self.model.objects.filter(name__icontains=self.kwargs['name'])[:]
