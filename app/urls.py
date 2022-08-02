from django.urls import *
from . import views

urlpatterns = [
    path('', views.EstudanteList.as_view(), name='estudante_list'),
    path('view/<int:pk>', views.EstudanteDetail.as_view(), name='estudante_detail'),
    path('new', views.EstudanteCreate.as_view(), name='estudante_new'),
    path('edit/<int:pk>', views.EstudanteUpdate.as_view(), name='estudante_edit'),
    path('delete/<int:pk>', views.EstudanteDelete.as_view(), name='estudante_delete'),
]