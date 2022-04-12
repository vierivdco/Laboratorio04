from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detalle, name='detalle'),
    path('<int:id>/resultados/', views.resultados, name='resultados'),
    path('<int:id>/voto/',views.votar, name='votar'),
]