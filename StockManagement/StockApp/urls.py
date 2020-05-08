#from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('view_raw_material', views.view_raw_material, name='view_raw_material'),
    # path('create_raw_material', views.create_raw_material, name='create_raw_material'),
    # path('update_raw_material/<str:name>', views.update_raw_material, name='update_raw_material'),
    # path('view_production_stage', views.view_production_stage, name='view_production_stage'),
    # path('create_production_stage', views.create_raw_material, name='create_production_stage'),
    # path('update_production_stage/<str:name>/<int:ratio>', views.update_production_stage, name='update_production_stage'),
    # path('view_dispatch', views.view_dispatch, name='view_dispatch'),
    # path('create_dispatch', views.create_dispatch, name='create_dispatch'),
    # path('update_dispatch/<str:name>', views.update_dispatch, name='update_dispatch'),
    # path('login',views.LoginView,name='login'),
    # path('expand/<str:name>',views.expand_raw_material,name='expand'),
    # #path('info',views.sys_info,name='sys_info'),
    # path('summary',views.summary_save,name='summary'),
    path('view_raw_material', RawMaterialDisplayView.as_view(),name='view_raw_material'),
    path('create_raw_material',RawMaterialCreateView.as_view(),name='create_raw_material'),
    path('expand_raw_material/<str:name>',ExpandRawMaterialView.as_view(),name='expand_raw_material'),

]
