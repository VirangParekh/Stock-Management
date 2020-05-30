#from django.contrib import admin
from django.urls import path
from .views import *
from.import views

urlpatterns = [
    path('view_raw_material', RawMaterialDisplayView.as_view(),name='view_raw_material'),
    path('create_raw_material',RawMaterialCreateView.as_view(),name='create_raw_material'),
    path('update_raw_material/<int:raw_material_ID>', views.RawMaterialUpdateView),
    # path('expand_raw_material/<str:name>',ExpandRawMaterialView.as_view(),name='expand_raw_material'),
    path('view_production_stage', ProductionStageDisplayView.as_view(),name='view_production_stage'),
    path('create_product', ProductionStageCreateView.as_view(),name='create_product'),
    path('update_product/<int:pk>',ProductionStageUpdateView.as_view(), name='update_product'),    
    path('view_dispatch',DispatchDisplayView.as_view(),name='view_dispatch'),
    path('create_dispatch',DispatchCreateView.as_view(),name='create_dispatch'),
    path('update_dispatch',DispatchUpdateView.as_view(),name='update_dispatch'),
    path('',LoginView.as_view(),name='login'),
]
