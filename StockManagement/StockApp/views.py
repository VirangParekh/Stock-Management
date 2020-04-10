from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import RawMaterial, ProductionStage, Dispatch
from .forms import RawMaterialForm, ProductionStageForm, DispatchForm #LoginForm
import templates
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
#from django.shortcuts import redirect

# class RawMaterialView(UpdateView):
#     model=RawMaterial
#     fields=['quantity']
#     form_class=RawMaterialForm
#     template_name='RawMaterial.html'



def view_raw_material(request):
    all_raw_material=RawMaterial.objects.all()
    form=RawMaterialForm()
    return render(request, 'RawMaterial.html', {'all_raw_material':all_raw_material,'create_form':form})

def create_raw_material(request):
    form=RawMaterialForm()
    if request.method == 'POST':
        form=RawMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_raw_material')
    return render(request, 'RawMaterial.html', {'create_form':form})

def update_raw_material(request, name):
    raw_material=RawMaterial.objects.get(name=name)
    form=RawMaterialForm(instance=raw_material)
    if request.method == 'POST':
        form=RawMaterialForm(request.POST, instance=raw_material)
        if form.is_valid():
            form.save()
            return redirect('/view_raw_material')
    return render(request, 'RawMaterial.html', {'update_form':form})


def view_production_stage(request):
    all_products=ProductionStage.objects.all()
    form=ProductionStageForm()
    return render(request, 'ProductionStage.html', {'all_products':all_products,'create_form':form})

def create_product(request):
    form=ProductionStageForm()
    if request.method == 'POST':
        form=ProductionStageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_production_stage')
    return render(request, 'ProductionSTage.html', {'create_form':form})

def update_production_stage(request, name):
    product=ProductionStage.objects.get(name=name)
    form=ProductionStageForm(instance=product)
    if request.method == 'POST':
        form=RawMaterialForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/view_production_stage')
    return render(request, 'RawMaterial.html', {'update_form':form})

def view_dispatch(request):
    all_products=Dispatch.objects.all()
    return render(request, 'Dispatch.html', {'all_products':all_products})

def create_dispatch(request):
    form=DispatchForm()
    if request.method == 'POST':
        form=DispatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_dispatch')
    return render(request, 'Dispatch.html', {'create_form':form})

def update_dispatch(request, name):
    product=Dispatch.objects.get(name=name)
    form=DispatchForm(instance=product)
    if request.method == 'POST':
        form=DispatchForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/view_dispatch')
    return render(request, 'Dispatch.html', {'update_form':form})

def LoginView(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        form.fields['username'].widget.attrs['class']={"form-control form-group",}
        form.fields['password'].widget.attrs['class']={"form-control form-group"}
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('/view_raw_material')
    else:
        form=AuthenticationForm()

    return render(request, 'Login.html', {'form':form})


