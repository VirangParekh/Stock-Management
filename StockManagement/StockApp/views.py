from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, Page
from .forms import *
from datetime import date
#import templates.virang_templates


class RawMaterialDisplayView(ListView):
    model = RawMaterial
    context_object_name = 'view_raw_material'
    queryset = RawMaterial.objects.all()
    template_name = 'StockApp/rawmaterial_list.html'


class RawMaterialCreateView(CreateView):
    form_class = RawMaterialForm
    # fields='__all__'
    template_name = 'StockApp/rawmaterial_create.html'
    success_url = '/view_raw_material'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.mode == 'ltr':
            rate = self.object.rate
            density = self.object.density
            rate = rate/density
            self.object.rate = rate
            self.object.save()
            return HttpResponseRedirect(self.success_url)


class RawMaterialUpdateView(UpdateView):
    model = RawMaterial
    fields = [
        'quantity',
        'selected',
        'date',
    ]
    template_name = 'StockApp/rawmaterial_update.html'
    success_url = '/view_raw_material'
    # queryset=RawMaterial.objects.all()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.selected == True:
            quantity_old = getattr(RawMaterial.objects.get(
                pk=self.object.pk), 'quantity')
            quantity_incoming = self.object.quantity
            quantity_new = quantity_old+quantity_incoming
            self.object.quantity = quantity_new
            self.object.save()
            return HttpResponseRedirect(self.success_url)


class ExpandRawMaterialView(ListView):
    model = RawMaterial
    context_object_name = 'expand_raw_material'
    template_name = 'StockApp/expand_list.html'

    def get_queryset(self, **kwargs):
        return self.model.objects.filter(name__icontains=self.kwargs['name'])[:]


class ProductionStageDisplayView(ListView):
    model = ProductionStage
    context_object_name = 'view_production_stage'
    queryset = ProductionStage.objects.all()
    # paginate_by=5
    template_name = 'StockApp/productionstage_list.html'


class ProductionStageCreateView(CreateView):
    model = ProductionStage
    fields = '__all__'
    template_name = 'StockApp/productionstage_create.html'
    success_url = '/view_production_stage'


class DispatchDisplayView(ListView):
    model = Dispatch
    template_name = 'StockApp/dispatch_list.html'
    queryset = Dispatch.objects.all()


class DispatchCreateView(CreateView):
    model = Dispatch
    fields = '__all__'
    template_name = 'StockApp/dispatch_create.html'
    success_url = '/view_dispatch'
    # context_object_name='new_dispatch'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.success_url)


class DispatchUpdateView(UpdateView):
    model = Dispatch
    fields = [
        'date_dispatch',
        'bill_no',
        'dispatch_status',
    ]
    template_name = 'StockApp/dispatch_update.html'
    success_url = '/view_dispatch'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.dispatch_status == 'True':
            self.object.save()
            return HttpResponseRedirect(self.success_url)
