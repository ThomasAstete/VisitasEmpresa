from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_visita, name='registrar_visita'),
    path('lista/', views.lista_visitas, name='lista_visitas'),
    path('salida/<int:visita_id>/', views.registrar_salida, name='registrar_salida'),
]