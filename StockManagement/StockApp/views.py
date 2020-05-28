from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.views.generic import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.paginator import Paginator, Page
from .forms import *
from datetime import date
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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


def RawMaterialUpdateView(request, sr):

    if request.method == "POST":
        quantity_incoming = int(request.POST["new_quantity"])
        quantity_old = getattr(RawMaterial.objects.get(
            pk=int(sr)), 'quantity')
        quantity_new = quantity_old+quantity_incoming
        RawMaterial.objects.filter(pk=int(sr)).update(quantity=quantity_new)
        return HttpResponseRedirect('/view_raw_material')


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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        cores_raw_materials = ProductionStage.objects.values_list(
            'id', 'raw_materials')
        prod_quantity_list = [
            self.object.quantity1,
            self.object.quantity2,
            self.object.quantity3,
            self.object.quantity4,
            self.object.quantity5,
            self.object.quantity6,
            self.object.quantity7,
        ]
        count_index = 0
        for i in cores_raw_materials:
            if self.object.pk == i[0]:
                raw_material = RawMaterial.objects.filter(id=i[1])
                quantity = getattr(raw_material, 'quantity')
                quantity -= prod_quantity_list[count_index]
                count_index += 1
                raw_material.quantity = quantity
                raw_material.save()
        return HttpResponseRedirect(self.success_url)


class ProductionStageUpdateView(UpdateView):
    model = ProductionStage
    fields = '__all__'
    template_name = 'StockApp/productionstage_update.html'
    success_url = '/update_production_stage'


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
        cores_products = Dispatch.objects.values_list('id', 'raw_materials')
        prod_quantity_list = [
            self.object.quantity1,
            self.object.quantity2,
            self.object.quantity3,
            self.object.quantity4,
            self.object.quantity5,
            self.object.quantity6,
            self.object.quantity7,
        ]
        count_index = 0
        for i in cores_products:
            if self.object.pk == i[0]:
                product = ProductionStage.objects.filter(id=i[1])
                quantity = getattr(product, 'quantity')
                quantity -= prod_quantity_list[count_index]
                count_index += 1
                product.quantity = quantity
                product.save()
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


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'StockApp/login.html'
    success_url = '/view_raw_material'
