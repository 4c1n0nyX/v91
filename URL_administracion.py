from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('administracion', views.administracion, name="administracion"),
    path('adminbienes', views.adminbienes, name="adminbienes"),
    path('adminbienes<str:accion>', views.adminbienes_consultar, name="adminbienes_consultar"),
    path('adminbienes/update/<int:id>', views.update_adminbienes, name="update_adminbienes"),
    path('adminbienes/delete/<int:id>', views.del_adminbienes, name="del_adminbienes"),
    path('compras', views.compras, name="compras"),
    path('compras<str:accion>', views.compras_consultar, name="compras_consultar"),
    path('compras/update/<int:id>', views.update_compras, name="update_compras"),
    path('compras/delete/<int:id>', views.del_compras, name="del_compras"),
    #path('consumible', views.consumible, name="consumible"),
    #path('vehiculos', views.vehiculos, name="vehiculos"),
]
